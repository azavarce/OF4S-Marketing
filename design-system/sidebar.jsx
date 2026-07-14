// Shared sidebar — emit on every page. Pass `current` to highlight active link.
// On mobile: renders a top bar with a hamburger that toggles the sidebar as a drawer.

function DSSidebar({ current = 'index' }) {
  const [open, setOpen] = React.useState(false);
  const [topbarHost, setTopbarHost] = React.useState(null);

  // Mount the topbar at the top of <body> so position:sticky works regardless
  // of where DSSidebar is rendered in the page (most pages render it inside
  // a grid cell that would prevent sticky from working).
  React.useEffect(() => {
    let host = document.getElementById('ds-topbar-host');
    if (!host) {
      host = document.createElement('div');
      host.id = 'ds-topbar-host';
      host.style.display = 'contents';
      document.body.insertBefore(host, document.body.firstChild);
    } else {
      host.style.display = 'contents';
    }
    setTopbarHost(host);
  }, []);

  // Close drawer on route nav (link clicks) + escape key
  React.useEffect(() => {
    function onKey(e) { if (e.key === 'Escape') setOpen(false); }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  // Lock body scroll while drawer is open on mobile
  React.useEffect(() => {
    if (open) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => { document.body.style.overflow = ''; };
  }, [open]);

  const sections = [
    {
      label: 'Brand',
      items: [
        { id: 'index',      num: '00', label: 'Overview',     href: 'index.html' },
        { id: 'directions', num: '★',  label: 'Direction', href: 'directions.html' },
        { id: 'logo-type', num: '01', label: 'Logo & Type', href: 'logo-type.html' },
      ],
    },
    {
      label: 'Foundations',
      items: [
        { id: 'color',     num: '02', label: 'Color',        href: 'color.html' },
        { id: 'type',      num: '03', label: 'Typography',   href: 'typography.html' },
        { id: 'iconography', num: '04', label: 'Iconography', href: 'iconography.html' },
        { id: 'imagery',   num: '05', label: 'Imagery',      href: 'imagery.html' },
      ],
    },
    {
      label: 'Components',
      items: [
        { id: 'components', num: '06', label: 'UI Library',  href: 'components.html' },
      ],
    },
    {
      label: 'Templates',
      items: [
        { id: 'presentation', num: '07', label: 'Presentations', href: 'presentation.html' },
        { id: 'proposal',     num: '08', label: 'Proposals',     href: 'proposal.html' },
        { id: 'collateral',   num: '09', label: 'Collateral',    href: 'collateral.html' },
        { id: 'social',       num: '10', label: 'Social & web',  href: 'social.html' },
      ],
    },
  ];

  return (
    <React.Fragment>
      {/* Mobile top bar — portaled to body top so sticky works everywhere */}
      {topbarHost && ReactDOM.createPortal(
        <div className="ds-topbar">
          <a href="index.html" className="brand" style={{ textDecoration: 'none' }}>
            <span className="mark">OF<span style={{ color: 'var(--of4s-navy-300)' }}>4</span>S</span>
            <span className="label">Design&nbsp;System</span>
          </a>
          <button
            className="ds-burger"
            aria-label={open ? 'Close menu' : 'Open menu'}
            aria-expanded={open}
            onClick={() => setOpen(o => !o)}
          >
            {open ? (
              <svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" /></svg>
            ) : (
              <svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" /></svg>
            )}
          </button>
        </div>,
        topbarHost
      )}

      {/* Scrim */}
      <div
        className={`ds-scrim ${open ? 'open' : ''}`}
        onClick={() => setOpen(false)}
        aria-hidden="true"
      />

      {/* Sidebar (drawer on mobile, fixed sidebar on desktop) */}
      <aside className={`ds-sidebar ${open ? 'open' : ''}`}>
        <div className="ds-sidebar-brand">
          <span className="mark">OF<span style={{ color: 'var(--of4s-navy-300)' }}>4</span>S</span>
          <span className="label">Design&nbsp;System</span>
        </div>

        {sections.map(sec => (
          <div className="ds-nav-section" key={sec.label}>
            <h4>{sec.label}</h4>
            {sec.items.map(it => (
              <a
                key={it.id}
                href={it.href}
                className={`ds-nav-link ${current === it.id ? 'active' : ''}`}
                onClick={() => setOpen(false)}
              >
                <span>{it.label}</span>
                <span className="num">{it.num}</span>
              </a>
            ))}
          </div>
        ))}

        <div style={{ marginTop: 40, paddingTop: 24, borderTop: '1px solid rgba(255,255,255,0.08)' }}>
          <div className="ds-mono" style={{ color: 'rgba(255,255,255,0.4)', fontSize: 10 }}>
            v1.0 · April 2026
          </div>
          <div className="ds-mono" style={{ color: 'rgba(255,255,255,0.4)', fontSize: 10, marginTop: 4 }}>
            Office Furniture 4 Sale
          </div>
        </div>
      </aside>
    </React.Fragment>
  );
}

function DSFooter() {
  return (
    <footer className="ds-footer">
      <span>OF4S — Design System v1.0</span>
      <span className="acc">Local · Modern · Easy</span>
      <span>© 2026 Office Furniture 4 Sale</span>
    </footer>
  );
}

Object.assign(window, { DSSidebar, DSFooter });
