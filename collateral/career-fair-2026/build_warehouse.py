import sys, pathlib
S = pathlib.Path(sys.argv[1])
style = (S / "style.part").read_text().replace("</style>", """
  .page { page-break-after: always; }
  .loc { max-width: 70mm; }
  .body { padding-top: 7mm; }
  .bonus { margin-top: 12px; padding: 10px 12px; background: var(--paper-100); border-radius: 8px; }
  .bonus .k { font-family: var(--mono); font-size: 9.5px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--navy-600); margin-bottom: 6px; display: block; }
  .bonus li { margin-bottom: 4px; }
  .bonus li::before { content: "+"; background: none; border: 0; width: auto; height: auto; top: -1px; font-weight: 700; color: var(--navy-600); }
  .apply .addr { margin-top: 8px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.08em; color: var(--stone-600); }
</style>""")

T = {
 "en": dict(cap="Office Furniture 4 Sale · Since 2005", eyebrow="Now Hiring", title="Warehouse <em>Associate</em>",
   per="/ hour", k1="Schedule", v1="Full-time", k2="Hours", v2="37–40 / week",
   blabel="Benefits", benefits=["Health insurance", "401(k) + matching", "Paid time off", "Employee discount"],
   h_do="What you'll <em>do</em>",
   do=["<strong>Receive</strong> incoming products at the warehouse",
       "Do regular <strong>inventory counts</strong> so the system matches the shelves",
       "Put products away on the correct shelf",
       "Check that outgoing orders are complete and match the client's order",
       "Follow warehouse procedures"],
   h_need="What you <em>need</em>",
   need=["<strong>Speak English and Spanish</strong>",
         "Read and write in English",
         "Legally allowed to work in the U.S.",
         "Available at least 37 hours a week during business hours",
         "Comfortable working in a warehouse",
         "Detail-oriented, disciplined, and a good problem solver"],
   bk="Bonus if you have", bonus=["1 year of warehouse or shipping &amp; receiving experience", "Forklift certification"],
   apply="Scan to <em>apply</em> today",
   alt="No phone handy? <b>Talk to us at the booth</b> and leave your name and number.",
   qralt="QR code to apply on Indeed", ph="[Website · Phone]"),
 "es": dict(cap="Office Furniture 4 Sale · Desde 2005", eyebrow="Estamos contratando", title="Asociado de <em>Almacén</em>",
   per="/ hora", k1="Horario", v1="Tiempo completo", k2="Horas", v2="37–40 / semana",
   blabel="Beneficios", benefits=["Seguro médico", "401(k) con aporte", "Tiempo libre pagado", "Descuento de empleado"],
   h_do="Lo que vas a <em>hacer</em>",
   do=["<strong>Recibir</strong> la mercancía que llega al almacén",
       "Hacer <strong>conteos de inventario</strong> para que el sistema coincida con los estantes",
       "Colocar los productos en el estante correcto",
       "Verificar que los pedidos de salida estén completos y coincidan con el pedido del cliente",
       "Seguir los procedimientos del almacén"],
   h_need="Lo que <em>necesitas</em>",
   need=["<strong>Hablar inglés y español</strong>",
         "Leer y escribir en inglés",
         "Estar autorizado para trabajar en EE. UU.",
         "Disponibilidad de al menos 37 horas por semana en horario laboral",
         "Sentirte cómodo trabajando en un almacén",
         "Detallista, disciplinado y bueno resolviendo problemas"],
   bk="Un plus si tienes", bonus=["1 año de experiencia en almacén o envíos y recepción", "Certificación de montacargas"],
   apply="Escanea y <em>aplica</em> hoy",
   alt="¿No tienes tu teléfono a mano? <b>Habla con nosotros en el stand</b> y déjanos tu nombre y número.",
   qralt="Código QR para aplicar en Indeed", ph="[Sitio web · Teléfono]"),
}

def li(items): return "\n".join(f"        <li>{x}</li>" for x in items)

def page(t, lang):
    chips = "\n".join(f'      <span class="chip">{b}</span>' for b in t["benefits"])
    return f"""<div class="page" lang="{lang}">
  <header class="hero">
    <div class="top">
      <div>
        <div class="brand">OF<span class="four">4</span>S</div>
        <div class="brand-cap">{t['cap']}</div>
      </div>
      <div class="loc">Hialeah, FL<br>1790 W 8th Ave</div>
    </div>
    <div class="eyebrow">{t['eyebrow']}</div>
    <h1>{t['title']}</h1>
    <div class="facts">
      <div class="pay"><b>$15–16</b><span>{t['per']}</span></div>
      <div class="fact"><span class="k">{t['k1']}</span><span class="v">{t['v1']}</span></div>
      <div class="fact"><span class="k">{t['k2']}</span><span class="v">{t['v2']}</span></div>
    </div>
  </header>

  <section class="benefits">
    <span class="label">{t['blabel']}</span>
    <div class="chips">
{chips}
    </div>
  </section>

  <section class="body">
    <div>
      <h2>{t['h_do']}</h2>
      <ul>
{li(t['do'])}
      </ul>
    </div>
    <div class="req">
      <h2>{t['h_need']}</h2>
      <ul>
{li(t['need'])}
      </ul>
      <div class="bonus">
        <span class="k">{t['bk']}</span>
        <ul>
{li(t['bonus'])}
        </ul>
      </div>
    </div>
  </section>

  <section class="apply">
    <div class="qr"><img src="qr-warehouse.svg" alt="{t['qralt']}"></div>
    <div>
      <h3>{t['apply']}</h3>
      <p class="alt">{t['alt']}</p>
      <p class="addr">1790 W 8th Ave, Hialeah, FL 33010</p>
    </div>
  </section>

  <footer class="foot">
    <span>OF4S · South Florida</span>
    <span class="placeholder">{t['ph']}</span>
  </footer>
</div>"""

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>OF4S Warehouse Associate Flyer</title>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
{style}
</head>
<body>
{page(T['en'], 'en')}
{page(T['es'], 'es')}
</body>
</html>
"""
(S / "flyer-warehouse-associate.html").write_text(html)
