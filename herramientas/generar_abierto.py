"""Genera los PDF abiertos de «Mi mapa de 21 días» con la línea gráfica del Tour Intercolegial.

Reutiliza textos y diseño del motor del Tour (taller/_motor/generar.py): mismos colores, barra y
composición. Cambia lo que no viaja con la licencia o no es del equipo autor:
- la tipografía VAG (licenciada) se sustituye por Nunito (SIL OFL, en herramientas/fuentes/);
- el logo de la GEW y el espacio de patrocinadores salen; quedan los logos del equipo autor
  (Fundación Enlata, IAvanza, Fundación Ayudar Me Da Vida), tal cual, desde materiales/logos/;
- cada pieza lleva la línea de crédito obligatoria.

Uso:  /usr/local/bin/python3 generar_abierto.py
Sale en ../materiales/
Código bajo licencia MIT. Los PDF que produce, bajo CC BY-SA 4.0 (los logos quedan fuera: ver MARCA.md).
"""
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "taller/_motor"))
import generar as g  # noqa: E402

SALIDA = AQUI.parent / "materiales"
LOGOS = SALIDA / "logos"
FUENTES = AQUI / "fuentes"
LOGO_ENLATA = (LOGOS / "enlata-wordmark-color.svg").as_uri()
LOGO_IAVANZA = (LOGOS / "iavanza-lockup-color.svg").as_uri()
LOGO_AMDV = (LOGOS / "ayudar-me-da-vida-color.png").as_uri()

CREDITO = ("Material y contenido: equipo de Fundación Enlata, IAvanza y Fundación Ayudar Me Da Vida"
           " · Mi mapa de 21 días · CC BY-SA 4.0")
URL = "pgomez-enata.github.io/mi-mapa-21-dias"

g.SALIDA = SALIDA

FONT_FACE = "".join(
    f"@font-face {{ font-family: Nunito; font-weight: {peso}; src: url('{(FUENTES / f'Nunito-{n}.ttf').as_uri()}'); }}\n"
    for peso, n in ((300, "Light"), (700, "Bold"), (900, "Black")))

CSS_LOGOS = """
.logos.eq { gap: 7mm; }
.logos.eq .enl { height: 10mm; width: 29.1mm; }
.logos.eq .iav { height: 7.5mm; width: 40.8mm; }
.logos.eq .amdv { height: 21mm; width: 22.6mm; }
.logos.eq .cred { margin-left: auto; font-family: 'Noto Sans', sans-serif; font-size: 7.6pt; line-height: 1.3;
                  color: #333; text-align: right; max-width: 70mm; }
.proy .logos.eq .enl { height: 7.5mm; width: 21.8mm; } .proy .logos.eq .iav { height: 5.5mm; width: 29.9mm; }
.proy .logos.eq .amdv { height: 14mm; width: 15mm; } .proy .logos.eq .cred { font-size: 7pt; max-width: 120mm; }
"""


def logos_equipo():
    return (f'<div class="logos eq"><img class="enl" src="{LOGO_ENLATA}"><img class="iav" src="{LOGO_IAVANZA}">'
            f'<img class="amdv" src="{LOGO_AMDV}"><div class="cred">Material y contenido desarrollados por el equipo de '
            f'Fundación Enlata, IAvanza y Fundación Ayudar Me Da Vida<br>Mi mapa de 21 días · CC BY-SA 4.0 · {URL}</div></div>')


LOGOS_MAPA = (f'<div style="display:flex;align-items:center;gap:5mm;margin-top:2.5mm">'
              f'<img src="{LOGO_ENLATA}" style="height:6mm"><img src="{LOGO_IAVANZA}" style="height:4.4mm">'
              f'<img src="{LOGO_AMDV}" style="height:12mm"></div>')


LOGOS_CAB = (f'<div style="display:flex;align-items:center;gap:4mm">'
             f'<img src="{LOGO_ENLATA}" style="height:5mm"><img src="{LOGO_IAVANZA}" style="height:3.6mm">'
             f'<img src="{LOGO_AMDV}" style="height:10mm"></div>')


def tour(html):
    html = re.sub(r"@font-face \{[^}]*\}\s*", "", html)
    html = html.replace("<style>", "<style>" + FONT_FACE, 1).replace("font-family: VAG", "font-family: Nunito")
    html = re.sub(r'<div class="logos">.*?<div class="patro">.*?</div></div></div>', logos_equipo(), html, flags=re.S)
    html = re.sub(r'<div class="logos">.*?</div>', logos_equipo(), html, flags=re.S)
    html = html.replace('<div class="sub">Tour Intercolegial · Semana Global de Emprendimiento<br>República Dominicana 2026</div>',
                        LOGOS_CAB)
    html = html.replace("Fundación Ayudar Me Da Vida · Fundación Enlata · IAvanza · GEW República Dominicana", CREDITO)
    html = html.replace("Tour Intercolegial · GEW RD 2026", CREDITO)
    html = html.replace("</body></html>", LOGOS_MAPA + "</body></html>") if "Mi trabajo" in html else html
    html = html.replace("____ / ____ / 2026", "____ / ____ / ______")
    html = html.replace("</style>", CSS_LOGOS + "</style>", 1)
    html = html.replace('<div class="p">', '<div class="p proy">')
    return html


def manual_pdf():
    from weasyprint import CSS, HTML
    from weasyprint.text.fonts import FontConfiguration
    fc = FontConfiguration()
    html = subprocess.run(["pandoc", str(AQUI.parent / "MANUAL-METODOLOGICO.md"), "-f", "gfm", "-t", "html5", "-s",
                           "--metadata", "title= "], capture_output=True, text=True, check=True).stdout
    cabecera = (f'<div class="cabecera">{g.barra("5pt")}<div class="lg"><img class="enl" src="{LOGO_ENLATA}">'
                f'<img class="iav" src="{LOGO_IAVANZA}"><img class="amdv" src="{LOGO_AMDV}"></div></div>')
    html = html.replace("<body>", "<body>" + cabecera, 1)
    css = FONT_FACE + g.CSS_DOC + f"""
h1,h2{{font-family:Nunito !important;font-weight:300;text-transform:uppercase;letter-spacing:.02em}}
h1{{font-size:24pt;border-top:0;padding-top:2mm}} h1+h2{{margin-top:0;color:{g.NARANJA}}}
.cabecera{{margin-bottom:5mm}} .lg{{display:flex;align-items:center;gap:8mm;padding:4mm 0 1mm}}
.lg .enl{{height:9mm}} .lg .iav{{height:6.5mm}} .lg .amdv{{height:19mm}}
@page{{@bottom-left{{content:'{CREDITO}';font-size:6.6pt;color:#777}}}}"""
    HTML(string=html).write_pdf(SALIDA / "MANUAL-METODOLOGICO.pdf", stylesheets=[CSS(string=css, font_config=fc)],
                                 font_config=fc)


def main():
    SALIDA.mkdir(exist_ok=True)
    for viejo in SALIDA.glob("*.pdf"):
        viejo.unlink()
    manual_pdf()
    g.CSS_BASE = tour(g.CSS_BASE)
    g.CSS_LAMINA = tour(g.CSS_LAMINA)
    g.CSS_PROY = tour(g.CSS_PROY)
    pdf = lambda html, nombre: g.a_pdf(tour(html), nombre)  # noqa: E731
    f = pdf(g.html_frente(False), "_frente.pdf")
    d = pdf(g.html_dorso(False), "_dorso.pdf")
    g.unir([f, d], SALIDA / "MAPA-21-DIAS-carta-BN-doble-cara.pdf")

    lam = g.PdfReader(pdf(g.html_laminas(), "_laminas.pdf")).pages
    mapa = g.PdfReader(pdf(g.html_frente(True), "_mapa_color.pdf")).pages[0]
    escritor = g.PdfWriter()
    for p in [lam[0], lam[1], lam[2], mapa, lam[3], lam[4]]:
        escritor.add_page(p)
    with open(SALIDA / "LAMINAS-6-carta-color.pdf", "wb") as fh:
        escritor.write(fh)
    cache = AQUI / "_cache_mapa"
    subprocess.run(["pdftoppm", "-r", "150", "-png", "-singlefile", str(SALIDA / "_mapa_color.pdf"), str(cache)], check=True)
    pdf(g.html_presentacion((AQUI / "_cache_mapa.png").as_uri()), "PRESENTACION-AULA-16x9.pdf")
    subprocess.run(["cp", str(AQUI / "_cache_mapa.png"), str(AQUI / "_mapa_color.png")], check=True)
    (AQUI / "_cache_mapa.png").unlink()
    (SALIDA / "_laminas.pdf").unlink()
    (SALIDA / "_mapa_color.pdf").unlink()
    for p in sorted(SALIDA.glob("*.pdf")):
        print(p)


if __name__ == "__main__":
    main()
