import sys, pathlib
S = pathlib.Path(sys.argv[1])
style = (S / "style.part").read_text().replace("</style>", """
  .page { page-break-after: always; }
  .page[lang=es] .eyebrow { margin-top: 9mm; }
  .page[lang=es] .body { padding-top: 7mm; }
  .page[lang=es] li { margin-bottom: 5px; }
  .page[lang=es] h1 { font-size: 52px; }
  .page[lang=es] .chip { font-size: 12.5px; padding: 6px 10px; }
</style>""")

T = {
 "en": dict(cap="Office Furniture 4 Sale · Since 2005", loc="Hialeah, FL<br>Distribution Center",
   eyebrow="Now Hiring", title="Furniture Delivery Driver &amp; <em>Warehouse</em>",
   per="/ hour", k1="Schedule", v1="Full-time", k2="Start time", v2="6–7 AM",
   blabel="Benefits", benefits=["Health insurance", "401(k) + matching", "Paid time off", "Referral program"],
   h_do="What you'll <em>do</em>",
   do=["Load your truck and check the packing lists against the day's routes",
       "<strong>Deliver and install</strong> office furniture with your team",
       "Call clients during the day with your ETA",
       "Leave every space clean: remove cartons and debris, vacuum",
       "Report delays, damage, or missing items to the office",
       "Keep your truck clean and report any maintenance issues",
       "Help in the warehouse on days with no deliveries"],
   h_need="What you <em>need</em>",
   need=["<strong>Valid, clean Florida driver's license</strong>",
         "<strong>1+ year</strong> box truck or delivery driver experience",
         "Fluent in English",
         "High school diploma or equivalent",
         "Able to lift heavy furniture",
         "Clean, professional appearance",
         "Background check and drug test before your first day"],
   apply="Scan to <em>apply</em> today", s1="Submit your resume", s2="In-person interview",
   alt="No phone handy? <b>Talk to us at the booth</b> and leave your name and number.",
   qralt="QR code to apply on Indeed", ph="officefurniture4sale.com"),
 "es": dict(cap="Office Furniture 4 Sale · Desde 2005", loc="Hialeah, FL<br>Centro de distribución",
   eyebrow="Estamos contratando", title="Chofer de Entrega de Muebles y <em>Almacén</em>",
   per="/ hora", k1="Horario", v1="Tiempo completo", k2="Hora de entrada", v2="6–7 AM",
   blabel="Beneficios", benefits=["Seguro médico", "401(k) con aporte", "Días pagados", "Programa de referidos"],
   h_do="Lo que vas a <em>hacer</em>",
   do=["Cargar tu camión y verificar las listas de empaque con las rutas del día",
       "<strong>Entregar e instalar</strong> muebles de oficina con tu equipo",
       "Llamar a los clientes durante el día para darles tu hora de llegada",
       "Dejar cada espacio limpio: retirar cajas y escombros, y aspirar",
       "Reportar a la oficina retrasos, daños o artículos faltantes",
       "Mantener tu camión limpio y reportar cualquier problema mecánico",
       "Ayudar en el almacén los días sin entregas"],
   h_need="Lo que <em>necesitas</em>",
   need=["<strong>Licencia de conducir de Florida válida y limpia</strong>",
         "<strong>1+ año</strong> de experiencia como chofer de entregas o de camión de caja",
         "Hablar inglés con fluidez",
         "Diploma de secundaria o equivalente",
         "Poder levantar muebles pesados",
         "Apariencia limpia y profesional",
         "Verificación de antecedentes y prueba de drogas antes de empezar"],
   apply="Escanea y <em>aplica</em> hoy", s1="Envía tu currículum", s2="Entrevista en persona",
   alt="¿No tienes tu teléfono a mano? <b>Habla con nosotros en el stand</b> y déjanos tu nombre y número.",
   qralt="Código QR para aplicar en Indeed", ph="officefurniture4sale.com"),
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
      <div class="loc">{t['loc']}</div>
    </div>
    <div class="eyebrow">{t['eyebrow']}</div>
    <h1>{t['title']}</h1>
    <div class="facts">
      <div class="pay"><b>$17</b><span>{t['per']}</span></div>
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
    </div>
  </section>

  <section class="apply">
    <div class="qr"><img src="qr.svg" alt="{t['qralt']}"></div>
    <div>
      <h3>{t['apply']}</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span>{t['s1']}</div>
        <div class="step"><span class="n">2</span>{t['s2']}</div>
      </div>
      <p class="alt">{t['alt']}</p>
    </div>
  </section>

  <footer class="foot">
    <span>OF4S · South Florida</span>
    <span class="site">{t['ph']}</span>
  </footer>
</div>"""

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>OF4S Delivery Driver Flyer</title>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
{style}
</head>
<body>
{page(T['en'], 'en')}
{page(T['es'], 'es')}
</body>
</html>
"""
(S / "flyer-delivery-driver.html").write_text(html)
