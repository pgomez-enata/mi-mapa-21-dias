"""Genera la versión abierta (sin marcas) del mapa, las láminas y la presentación de «Mi mapa de 21 días».

Reutiliza los textos y el diseño del motor del Tour (taller/_motor/generar.py) y quita lo que no viaja
con la licencia: logos, colores de marca y la tipografía VAG. Usa Noto Sans (SIL OFL).

Uso:  /usr/local/bin/python3 generar_abierto.py
Sale en ../materiales/
Código bajo licencia MIT. Los PDF que produce, bajo CC BY-SA 4.0.
"""
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / "taller/_motor"))
import generar as g  # noqa: E402

SALIDA = AQUI.parent / "materiales"
ACENTO = "#1F6F78"
FONDO = "#1E2326"
BARRA = ["#1F6F78", "#3E9AA3", "#8CC7CC"]
LICENCIA = "Mi mapa de 21 días · manual metodológico abierto · CC BY-SA 4.0"

g.SALIDA = SALIDA
g.NARANJA = ACENTO
g.CARBON = FONDO
g.BARRA = BARRA
g.TINTA = "#111"


def neutral(html):
    html = re.sub(r"@font-face \{[^}]*\}\s*", "", html)
    html = html.replace("font-family: VAG", "font-family: 'Noto Sans'")
    html = re.sub(r'<div class="logos">.*?</div></div>(?=</div>)', f'<div class="logos lic">{LICENCIA}</div>', html, flags=re.S)
    html = re.sub(r'<div class="logos">.*?</div>', f'<div class="logos lic">{LICENCIA}</div>', html, flags=re.S)
    html = html.replace("Tour Intercolegial · Semana Global de Emprendimiento<br>República Dominicana 2026",
                        "Un plan de una hoja<br>para lo que quieres mejorar")
    html = html.replace("Fundación Ayudar Me Da Vida · Fundación Enlata · IAvanza · GEW República Dominicana", LICENCIA)
    html = html.replace("Tour Intercolegial · GEW RD 2026", LICENCIA)
    html = html.replace("____ / ____ / 2026", "____ / ____ / ______")
    html = html.replace("</style>", ".lic{font-size:10pt;color:#333;justify-content:center}</style>", 1)
    for viejo, nuevo in (("#FFE9D6", "#DDEFF0"), ("#ff6b00", ACENTO)):
        html = html.replace(viejo, nuevo)
    return html


def recolorear():
    g.CSS_BASE = neutral(g.CSS_BASE)
    for nombre in ("CSS_LAMINA", "CSS_PROY"):
        css = getattr(g, nombre)
        for viejo, nuevo in ((g.TOK["color"]["campana2026"]["naranja"]["hex"], ACENTO),
                             (g.TOK["color"]["campana2026"]["carbon"]["hex"], FONDO)):
            css = css.replace(viejo, nuevo)
        setattr(g, nombre, neutral(css))


def manual_pdf():
    from weasyprint import CSS, HTML
    html = subprocess.run(["pandoc", str(AQUI.parent / "MANUAL-METODOLOGICO.md"), "-f", "gfm", "-t", "html5", "-s",
                           "--metadata", "title= "], capture_output=True, text=True, check=True).stdout
    css = g.CSS_DOC.replace(g.TOK["color"]["campana2026"]["naranja"]["hex"], ACENTO).replace("#c45a00", ACENTO)
    css = css.replace("#fff6ee", "#eef6f7") + "@page{@bottom-left{content:'%s';font-size:7pt;color:#777}}" % LICENCIA
    HTML(string=html).write_pdf(SALIDA / "MANUAL-METODOLOGICO.pdf", stylesheets=[CSS(string=css)])


def main():
    SALIDA.mkdir(exist_ok=True)
    manual_pdf()
    recolorear()
    pdf = lambda html, nombre: g.a_pdf(neutral(html), nombre)  # noqa: E731
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
    (AQUI / "_cache_mapa.png").unlink()
    (SALIDA / "_laminas.pdf").unlink()
    (SALIDA / "_mapa_color.pdf").unlink()
    for p in sorted(SALIDA.glob("*.pdf")):
        print(p)


if __name__ == "__main__":
    main()
