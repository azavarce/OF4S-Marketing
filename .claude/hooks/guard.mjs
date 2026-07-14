#!/usr/bin/env node
/**
 * OF4S Marketing — repo guard (PreToolUse hook)
 *
 * Two protections, enforced before any file-mutating tool runs:
 *
 *   1. LOCK the design system.  `design-system/**` is the canonical OF4S v3
 *      brand source of truth and must never change from an agent session.
 *      Any Edit/Write/MultiEdit/NotebookEdit into it is DENIED outright, and
 *      common file-mutating Bash commands aimed at it are DENIED too.
 *
 *   2. AUTHORIZE skill / guard changes.  Edits to the `of4s-blog-post` skill
 *      (and to this guard + settings.json that enforce it) are rare and
 *      consequential, so they require an explicit human OK.  The hook returns
 *      an "ask" decision with a plain-language prompt instead of allowing the
 *      edit silently.
 *
 * Everything else is left alone (decision "allow" is NOT returned, so normal
 * permission handling applies).
 *
 * Hook contract: reads a PreToolUse event as JSON on stdin, writes a JSON
 * decision on stdout. See https://docs.claude.com/en/docs/claude-code/hooks
 */

import path from "node:path";

// ---- Protected areas (relative to the repo root) ---------------------------

// Fully locked — no agent edits, ever.
const LOCKED = ["design-system"];

// Changes allowed only with an explicit human yes.
const AUTHORIZE = [
  ".claude/skills/of4s-blog-post",
  ".claude/hooks/guard.mjs",
  ".claude/settings.json",
];

// ---- Helpers ---------------------------------------------------------------

function readStdin() {
  return new Promise((resolve) => {
    let data = "";
    process.stdin.setEncoding("utf8");
    process.stdin.on("data", (c) => (data += c));
    process.stdin.on("end", () => resolve(data));
    // If nothing is piped, don't hang forever.
    setTimeout(() => resolve(data), 2000).unref?.();
  });
}

function emit(decision, reason) {
  process.stdout.write(
    JSON.stringify({
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: decision, // "deny" | "ask"
        permissionDecisionReason: reason,
      },
    })
  );
  process.exit(0);
}

function allowSilently() {
  // No decision => fall through to normal permission handling.
  process.exit(0);
}

// Normalize a candidate path to a repo-relative POSIX path, or null if it
// clearly falls outside the repo.
function relToRepo(root, candidate) {
  if (!candidate || typeof candidate !== "string") return null;
  const abs = path.isAbsolute(candidate)
    ? candidate
    : path.resolve(root, candidate);
  const rel = path.relative(root, abs);
  if (rel.startsWith("..") || path.isAbsolute(rel)) return null;
  return rel.split(path.sep).join("/");
}

// Does a repo-relative path sit inside one of the listed areas?
function within(rel, areas) {
  if (!rel) return false;
  return areas.some((a) => rel === a || rel.startsWith(a + "/"));
}

// Best-effort: does a Bash command look like it MUTATES a design-system path?
// Reads (cat/grep/ls/head/tail) are intentionally left alone.
function bashMutatesLocked(cmd) {
  if (typeof cmd !== "string" || !/design-system/.test(cmd)) return false;
  // Redirection into a design-system path:  > design-system/...  or  >> ...
  if (/>>?\s*['"]?[^\s'"|;&]*design-system/.test(cmd)) return true;
  // Destructive / in-place ops naming a design-system path.
  if (/\b(rm|rmdir|unlink|truncate|shred|dd)\b[^\n|;&]*design-system/.test(cmd))
    return true;
  if (/\bsed\b[^\n|;&]*-i[^\n|;&]*design-system/.test(cmd)) return true;
  if (/\b(mv|cp|install|ln|tee|rsync)\b[^\n|;&]*design-system/.test(cmd))
    return true;
  // chmod/chown on a design-system path.
  if (/\b(chmod|chown|chgrp)\b[^\n|;&]*design-system/.test(cmd)) return true;
  return false;
}

// ---- Main ------------------------------------------------------------------

const raw = await readStdin();
let event = {};
try {
  event = JSON.parse(raw || "{}");
} catch {
  // Malformed input — don't block the user, just get out of the way.
  allowSilently();
}

const root = process.env.CLAUDE_PROJECT_DIR || event.cwd || process.cwd();
const tool = event.tool_name || "";
const input = event.tool_input || {};

// File-editing tools: check the target path(s).
const FILE_TOOLS = new Set(["Edit", "Write", "MultiEdit", "NotebookEdit"]);
if (FILE_TOOLS.has(tool)) {
  const candidates = [input.file_path, input.notebook_path].filter(Boolean);
  for (const c of candidates) {
    const rel = relToRepo(root, c);
    if (within(rel, LOCKED)) {
      emit(
        "deny",
        `The OF4S design system is locked. \`${rel}\` is part of \`design-system/\`, ` +
          `which is the canonical brand source of truth and must not be modified in this ` +
          `session. If a design-system change is genuinely needed, it has to be made ` +
          `deliberately outside the normal agent flow.`
      );
    }
    if (within(rel, AUTHORIZE)) {
      emit(
        "ask",
        `Heads up: this edits \`${rel}\`, which changes the blog-creation skill (or the ` +
          `guard that protects it). That's a rare, consequential change. Are you sure you ` +
          `want to modify the skill? Confirm to proceed.`
      );
    }
  }
  allowSilently();
}

// Bash: best-effort guard against mutating the locked design system.
if (tool === "Bash") {
  if (bashMutatesLocked(input.command)) {
    emit(
      "deny",
      `That command looks like it would modify \`design-system/\`, which is locked. ` +
        `The OF4S design system is read-only in this session — reading it is fine, ` +
        `changing it is not.`
    );
  }
  allowSilently();
}

allowSilently();
