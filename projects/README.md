# projects/

One subfolder per marketing project. This is where the actual work lives — blog
posts, Instagram sets, email campaigns, flyers, one-off collateral, anything in
the OF4S marketing role. The `design-system/` at the repo root is the shared,
**read-only** brand source of truth that every project draws from.

## How a project works

Each project folder has its **own `CLAUDE.md`**. When you (or Claude) are working
inside that folder, Claude automatically reads that `CLAUDE.md` and follows it —
so every project can give Claude a **different behavior, checklist, and set of
guardrails** without them bleeding into each other. The root `CLAUDE.md` covers
the whole repo; the project `CLAUDE.md` layers project-specific instructions on
top.

```
projects/
├── README.md          ← you are here
├── _template/         ← copy this to start a new project type
│   └── CLAUDE.md
└── blog/              ← the "Explore Our Projects" blog workflow
    └── CLAUDE.md
```

## Start a new project type

Tell Claude, e.g. **"Set up a new Instagram project"** (or email campaign, flyer,
etc.). Claude will:

1. Copy `_template/` to `projects/<your-project>/`.
2. Work with you to fill in that project's `CLAUDE.md` — what the project is,
   how Claude should behave, the checklist of facts to collect, the output
   format, and any hard rules.
3. From then on, working inside `projects/<your-project>/` puts Claude in that
   project's mode.

You don't have to define everything up front — the behavior for each project
gets shaped as you build it out together.

## What stays off-limits

- **`design-system/`** is locked — projects *reference* it, never change it. A
  guard hook blocks edits to it.
- **`.claude/skills/of4s-blog-post/`** (the blog-creation skill) can only be
  changed with your explicit confirmation. See the root `README.md`.
