"""Genera los editables de «Mi mapa de 21 días» con la línea gráfica del Tour Intercolegial.

Sale en ../editables/:
- PRESENTACION-AULA-16x9.pptx     lámina 0 «quién soy» + las 6 del aula + créditos
- LAMINAS-6-carta.pptx            las 6 láminas para pegar, tamaño carta vertical
- MAPA-21-DIAS-carta.pptx         frente y dorso del mapa, todo en cajas y líneas editables
- MANUAL-METODOLOGICO.docx y las 4 plantillas en .docx

Abren en PowerPoint, Word, Google Slides, Google Docs, Keynote y LibreOffice. Tipografías: Nunito
(títulos) y Noto Sans (texto), las dos libres y disponibles en Google Fonts.
Los logos se insertan tal cual desde ../materiales/logos/ (no se recortan ni se recolorean).

Uso:  /usr/local/bin/python3 generar_editables.py   (después de generar_abierto.py, que deja _mapa_color.png)
Código bajo licencia MIT. Los editables, bajo CC BY-SA 4.0 (los logos quedan fuera: ver MARCA.md).
"""
import re
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Mm as DMm
from docx.shared import Pt as DPt
from docx.shared import RGBColor as DRGB
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Mm, Pt

AQUI = Path(__file__).resolve().parent
PAQ = AQUI.parent
sys.path.insert(0, str(AQUI.parents[1] / "taller/_motor"))
import generar as g  # noqa: E402

SALIDA = PAQ / "editables"
LOGOS = PAQ / "materiales/logos"
L_ENLATA = LOGOS / "enlata-wordmark-color-3000.png"
L_IAVANZA = LOGOS / "iavanza-lockup-color-2048.png"
L_AMDV = LOGOS / "ayudar-me-da-vida-color.png"
MAPA_PNG = AQUI / "_mapa_color.png"

TIT = "Nunito"
TXT = "Noto Sans"
NARANJA = RGBColor.from_string(g.NARANJA[1:])
CARBON = RGBColor.from_string(g.CARBON[1:])
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
NEGRO = RGBColor(0, 0, 0)
GRIS = RGBColor(0x55, 0x55, 0x55)
URL = "pgomez-enata.github.io/mi-mapa-21-dias"
CREDITO = ("Material y contenido desarrollados por el equipo de Fundación Enlata, IAvanza y Fundación Ayudar Me Da Vida"
           f" · Mi mapa de 21 días · CC BY-SA 4.0 · {URL}")
CREDITO_LARGO = ("Material y contenido del taller desarrollados por el equipo de Fundación Enlata, IAvanza y "
                 "Fundación Ayudar Me Da Vida para el Tour Intercolegial (República Dominicana, 2026). "
                 f"«Mi mapa de 21 días», licencia CC BY-SA 4.0: {URL}")


# ---------------------------------------------------------------- piezas comunes

def runs_html(par, html, tam, color, fuente=TIT, negrita=False, acento=NARANJA, mayus=False):
    """Escribe en el párrafo un texto con <b>…</b> (negrita en color de acento)."""
    for i, trozo in enumerate(re.split(r"</?b>", html)):
        if not trozo:
            continue
        r = par.add_run()
        r.text = trozo.upper() if mayus else trozo
        r.font.name = fuente
        r.font.size = Pt(tam)
        r.font.bold = negrita or i % 2 == 1
        r.font.color.rgb = acento if i % 2 == 1 else color


def caja_texto(sl, x, y, w, h, html, tam, color, fuente=TIT, negrita=False, mayus=False, alinear=None, ancla=None):
    tb = sl.shapes.add_textbox(Mm(x), Mm(y), Mm(w), Mm(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    if ancla:
        tf.vertical_anchor = ancla
    for i, linea in enumerate(html.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if alinear:
            p.alignment = alinear
        runs_html(p, linea, tam, color, fuente, negrita, mayus=mayus)
    return tb


def rect(sl, x, y, w, h, relleno=None, borde=None, grosor=1.0, forma=MSO_SHAPE.RECTANGLE, radio=None):
    s = sl.shapes.add_shape(forma, Mm(x), Mm(y), Mm(w), Mm(h))
    if relleno is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = relleno
    if borde is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = borde
        s.line.width = Pt(grosor)
    if radio is not None and forma == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radio
    s.shadow.inherit = False
    return s


def linea(sl, x1, y1, x2, y2, color=GRIS, grosor=0.6):
    c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Mm(x1), Mm(y1), Mm(x2), Mm(y2))
    c.line.color.rgb = color
    c.line.width = Pt(grosor)
    return c


def barra(sl, y, ancho, alto, color=True):
    if not color:
        rect(sl, 0, y, ancho, alto, relleno=NEGRO)
        return
    paso = ancho / len(g.BARRA)
    for i, hexa in enumerate(g.BARRA):
        rect(sl, i * paso, y, paso + 0.2, alto, relleno=RGBColor.from_string(hexa[1:]))


def logos(sl, x, y, alto_banda, escala, ancho_total, credito_tam):
    """Banda blanca con los tres logos tal cual (alto fijo, ancho proporcional) y la línea de crédito."""
    rect(sl, 0, y, ancho_total, alto_banda, relleno=BLANCO)
    cx = x
    medio = y + alto_banda / 2
    for ruta, alto in ((L_ENLATA, 9.5 * escala), (L_IAVANZA, 7 * escala), (L_AMDV, 19 * escala)):
        pic = sl.shapes.add_picture(str(ruta), Mm(cx), Mm(medio - alto / 2), height=Mm(alto))
        cx += pic.width / 36000 + 6 * escala
    caja_texto(sl, cx + 2, y + 2, ancho_total - cx - 2 - x, alto_banda - 4, CREDITO, credito_tam, GRIS, TXT,
               alinear=PP_ALIGN.RIGHT, ancla=MSO_ANCHOR.MIDDLE)


def vinetas(sl, x, y, w, items, tam, interlinea, color=BLANCO, columnas=1):
    por_col = -(-len(items) // columnas)
    ancho = (w - 8 * (columnas - 1)) / columnas
    for i, item in enumerate(items):
        col, fila = divmod(i, por_col)
        cx = x + col * (ancho + 8)
        cy = y + fila * interlinea
        linea(sl, cx, cy, cx + ancho, cy, RGBColor(0x88, 0x88, 0x88), 0.6)
        d = tam * 0.2
        rect(sl, cx, cy + interlinea / 2 - d / 2, d, d, relleno=NARANJA, forma=MSO_SHAPE.OVAL)
        caja_texto(sl, cx + d + 4, cy + 1.5, ancho - d - 4, interlinea - 2, item, tam, color, TXT,
                   ancla=MSO_ANCHOR.MIDDLE)


def fondo(sl, color):
    sl.background.fill.solid()
    sl.background.fill.fore_color.rgb = color


def nota(sl, texto):
    sl.notes_slide.notes_text_frame.text = texto


def oculta(sl):
    sl._element.set("show", "0")


NOTA_CREDITO = ("Si usas o adaptas este material, conserva la línea de crédito de la banda inferior y la lámina de "
                f"créditos. Crédito: {CREDITO_LARGO}. Si cambias el contenido, dilo («adaptado de…»). Ver MARCA.md.")


def lamina_creditos(prs, ancho, alto, vertical):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    fondo(sl, BLANCO)
    barra(sl, 0, ancho, 4)
    m = 18 if vertical else 20
    caja_texto(sl, m, 20, ancho - 2 * m, 12, "Créditos", 14, NARANJA, TIT, negrita=True, mayus=True)
    caja_texto(sl, m, 32, ancho - 2 * m, 30, "Mi mapa de <b>21 días</b>", 40 if vertical else 44, NEGRO, TIT, mayus=True)
    cuerpo = (f"{CREDITO_LARGO}\n\nAutores: Piero Gómez (Fundación Enlata · IAvanza) y Horacio de Windt "
              "(Fundación Ayudar Me Da Vida), con el equipo de facilitadores del Tour Intercolegial 2026.\n\n"
              "Inspirado en la investigación sobre contraste mental con intenciones de implementación "
              "(Gabriele Oettingen y Peter Gollwitzer). No está avalado por sus autores ni afiliado a WOOP.\n\n"
              "Si usas o adaptas este material: conserva esta lámina y la línea de crédito, di qué cambiaste "
              "y comparte tu versión con la misma licencia (CC BY-SA 4.0).")
    caja_texto(sl, m, 66 if vertical else 62, ancho - 2 * m, alto - 110, cuerpo, 15 if vertical else 16, NEGRO, TXT)
    logos(sl, m, alto - (34 if vertical else 30), 30 if vertical else 26, 1.3, ancho, 1)
    for sh in list(sl.shapes)[-1:]:
        sh.text_frame.text = ""
    nota(sl, NOTA_CREDITO)
    return sl


# ---------------------------------------------------------------- presentación 16:9

def presentacion():
    W, H = 338.7, 190.5
    prs = Presentation()
    prs.slide_width, prs.slide_height = Mm(W), Mm(H)
    vacia = prs.slide_layouts[6]

    sl = prs.slides.add_slide(vacia)
    fondo(sl, CARBON)
    barra(sl, 0, W, 4)
    caja_texto(sl, 20, 16, 150, 10, "Lámina 0 · Quién soy", 14, NARANJA, TIT, negrita=True, mayus=True)
    rect(sl, 20, 32, 70, 90, relleno=RGBColor(0x5E, 0x5E, 0x5E), forma=MSO_SHAPE.ROUNDED_RECTANGLE, radio=0.05)
    caja_texto(sl, 20, 72, 70, 10, "Tu foto (sin menores)", 12, BLANCO, TXT, alinear=PP_ALIGN.CENTER)
    caja_texto(sl, 104, 30, 214, 20, "Tu <b>nombre</b>", 44, BLANCO, TIT, mayus=True)
    vinetas(sl, 104, 56, 214, ["A qué me dedico, en una línea", "Algo que empecé y terminé", "Algo en lo que fallé"],
            22, 16)
    caja_texto(sl, 20, 140, 298, 20, "Máximo 30 segundos. No va: teléfono, correo, redes personales, precios, "
               "logos de tu empresa ni códigos QR.", 13, RGBColor(0xCC, 0xCC, 0xCC), TXT)
    logos(sl, 12, H - 17, 17, 0.75, W, 7)
    nota(sl, "Plantilla: cambia el texto por el tuyo. Contar a qué te dedicas no es vender. " + NOTA_CREDITO)

    lam = g.LAMINAS
    orden = [lam[0], lam[1], lam[2], None, lam[3], lam[4]]
    for item in orden:
        sl = prs.slides.add_slide(vacia)
        fondo(sl, CARBON)
        barra(sl, 0, W, 4)
        if item is None:
            if MAPA_PNG.exists():
                sl.shapes.add_picture(str(MAPA_PNG), Mm(20), Mm(13), height=Mm(156))
            caja_texto(sl, 155, 19, 165, 10, "Bloque 3 · Mi mapa", 14, NARANJA, TIT, negrita=True, mayus=True)
            caja_texto(sl, 155, 30, 165, 26, "Mi mapa de <b>21 días</b>", 44, BLANCO, TIT, mayus=True)
            vinetas(sl, 155, 60, 165, [
                "1 · Lo que voy a mejorar: una frase que se pueda ver", "2 · Cómo se verá el día 21",
                "3 · Lo que me puede frenar", "4 · Mi plan: «cuando…, voy a…» y «si pasa…, entonces yo…»",
                "Compañero/a de apoyo y las dos firmas", "Mi premio: «cuando lo logre, voy a…»", "El día 1 es hoy"],
                17, 13.5)
        else:
            num, tag, titulo, lead, items, remate = item
            caja_texto(sl, 20, 16, 150, 10, tag, 14, NARANJA, TIT, negrita=True, mayus=True)
            caja_texto(sl, 20, 27, 150, 58, titulo, 38, BLANCO, TIT, mayus=True)
            caja_texto(sl, 20, 90, 145, 50, lead, 20, BLANCO, TXT)
            dos = len(items) > 4
            vinetas(sl, 180, 26, 140, items, 17 if dos else 18, 12 if dos else 22)
            r = rect(sl, 20, H - 17 - 24 - 6, W - 40, 24, relleno=NARANJA, forma=MSO_SHAPE.ROUNDED_RECTANGLE, radio=0.2)
            caja_texto(sl, 27, H - 17 - 24 - 6 + 2, W - 54, 20, remate, 18, BLANCO, TIT, negrita=True,
                       ancla=MSO_ANCHOR.MIDDLE)
            del r
        logos(sl, 12, H - 17, 17, 0.75, W, 7)
        nota(sl, NOTA_CREDITO)
    lamina_creditos(prs, W, H, False)
    prs.save(SALIDA / "PRESENTACION-AULA-16x9.pptx")


# ---------------------------------------------------------------- láminas carta vertical

def laminas():
    W, H = 215.9, 279.4
    prs = Presentation()
    prs.slide_width, prs.slide_height = Mm(W), Mm(H)
    vacia = prs.slide_layouts[6]
    lam = g.LAMINAS
    for item in [lam[0], lam[1], lam[2], None, lam[3], lam[4]]:
        sl = prs.slides.add_slide(vacia)
        if item is None:
            fondo(sl, BLANCO)
            if MAPA_PNG.exists():
                sl.shapes.add_picture(str(MAPA_PNG), Mm(0), Mm(0), width=Mm(W), height=Mm(H))
            nota(sl, "Lámina 4 = el mapa a color. Para editarlo abre MAPA-21-DIAS-carta.pptx. " + NOTA_CREDITO)
            continue
        num, tag, titulo, lead, items, remate = item
        fondo(sl, CARBON)
        barra(sl, 0, W, 7)
        caja_texto(sl, 140, 160, 64, 60, num, 150, RGBColor(0x5C, 0x5C, 0x5C), TIT, negrita=True, alinear=PP_ALIGN.RIGHT)
        caja_texto(sl, 15, 21, 180, 10, tag, 13, NARANJA, TIT, negrita=True, mayus=True)
        caja_texto(sl, 15, 31, 186, 58, titulo, 44, BLANCO, TIT, mayus=True)
        caja_texto(sl, 15, 93, 172, 30, lead, 19, BLANCO, TXT)
        dos = len(items) > 6
        vinetas(sl, 15, 127, 186, items, 17 if dos else 18, 14 if dos else 16, columnas=2 if dos else 1)
        rect(sl, 15, H - 42 - 30, W - 30, 30, relleno=NARANJA, forma=MSO_SHAPE.ROUNDED_RECTANGLE, radio=0.15)
        caja_texto(sl, 23, H - 42 - 30 + 3, W - 46, 24, remate, 19, BLANCO, TIT, negrita=True, ancla=MSO_ANCHOR.MIDDLE)
        barra(sl, H - 33, W, 3)
        logos(sl, 9, H - 30, 30, 1.0, W, 7)
        nota(sl, NOTA_CREDITO)
    oculta(lamina_creditos(prs, W, H, True))
    prs.save(SALIDA / "LAMINAS-6-carta.pptx")


# ---------------------------------------------------------------- mapa carta (frente y dorso)

def caja(sl, x, y, w, h):
    return rect(sl, x, y, w, h, borde=NEGRO, grosor=1, forma=MSO_SHAPE.ROUNDED_RECTANGLE, radio=0.04)


def etiqueta(sl, x, y, n, titulo, ayuda, tam=12, ancho=180):
    cx = x
    if n:
        c = rect(sl, x, y, 6, 6, relleno=NEGRO, forma=MSO_SHAPE.OVAL)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        runs_html(p, n, 10, BLANCO, TIT, negrita=True)
        cx += 8.2
    t = caja_texto(sl, cx, y - 0.4, ancho, 7, "", tam, NEGRO)
    p = t.text_frame.paragraphs[0]
    runs_html(p, titulo, tam, NEGRO, TIT, negrita=True, mayus=True)
    if ayuda:
        r = p.add_run()
        r.text = "   " + ayuda
        r.font.name, r.font.size, r.font.italic = TXT, Pt(7.8), True
        r.font.color.rgb = RGBColor(0x44, 0x44, 0x44)


def renglones(sl, x, y, w, n, alto):
    for i in range(n):
        linea(sl, x, y + (i + 1) * alto, x + w, y + (i + 1) * alto, RGBColor(0x88, 0x88, 0x88), 0.6)


def cabecera(sl, titulo, sub, M, A):
    barra(sl, 9, 215.9, 1.8, color=False)
    caja_texto(sl, M, 13, 120, 12, titulo, 27, NEGRO, TIT, mayus=True)
    caja_texto(sl, M + A - 80, 15, 80, 10, sub, 7.4, RGBColor(0x33, 0x33, 0x33), TXT, alinear=PP_ALIGN.RIGHT)


def mapa():
    W, H = 215.9, 279.4
    M, A = 10, 195.9
    prs = Presentation()
    prs.slide_width, prs.slide_height = Mm(W), Mm(H)
    vacia = prs.slide_layouts[6]

    sl = prs.slides.add_slide(vacia)
    fondo(sl, BLANCO)
    cabecera(sl, "Mi mapa de <b>21 días</b>", "", M, A)
    cx = M + A - 62
    for ruta, alto in ((L_ENLATA, 5), (L_IAVANZA, 3.6), (L_AMDV, 10)):
        pic = sl.shapes.add_picture(str(ruta), Mm(cx), Mm(19 - alto / 2), height=Mm(alto))
        cx += pic.width / 36000 + 4
    caja_texto(sl, M, 27, A, 6, "Este mapa es de: ________________________________________________     "
               "Empecé el: ____ / ____ / ______", 9.5, NEGRO, TXT)
    y = 34
    caja(sl, M, y, A, 28)
    etiqueta(sl, M + 3.4, y + 2.4, "1", "Lo que voy a mejorar",
             "en una frase que se pueda ver: «voy a dormir antes de las 11», no «quiero ser mejor»")
    renglones(sl, M + 3.4, y + 8, A - 6.8, 2, 9.5)
    y = 65
    mitad = (A - 3) / 2
    for i, (n, t, ayuda) in enumerate((("2", "Cómo se verá cuando lo logre",
                                        "imagínate el día 21: ¿qué cambió? Léelo el día que se te quiten las ganas"),
                                       ("3", "Lo que me puede frenar", "¿qué de mí o de mi día puede hacer que lo deje?"))):
        x = M + i * (mitad + 3)
        caja(sl, x, y, mitad, 40)
        etiqueta(sl, x + 3.4, y + 2.4, n, t, "", ancho=mitad - 12)
        caja_texto(sl, x + 3.4, y + 9.5, mitad - 6.8, 6, ayuda, 7.8, RGBColor(0x44, 0x44, 0x44), TXT)
        renglones(sl, x + 3.4, y + 12, mitad - 6.8, 3, 8.5)
    y = 108
    caja(sl, M, y, A, 52)
    etiqueta(sl, M + 3.4, y + 2.4, "4", "Mi plan",
             "simple y con hora: lo que haces, cuándo, y qué haces si te frena lo de la caja 3")
    for j, (a, b) in enumerate((("Cuando", "voy a"), ("Si pasa", "entonces yo"))):
        yy = y + 11 + j * 11
        caja_texto(sl, M + 3.4, yy + 4, 25, 6, a, 10.5, NEGRO, TIT, negrita=True)
        linea(sl, M + 22, yy + 10, M + 98, yy + 10)
        caja_texto(sl, M + 100, yy + 4, 25, 6, b, 10.5, NEGRO, TIT, negrita=True)
        linea(sl, M + 124, yy + 10, M + A - 3.4, yy + 10)
    caja_texto(sl, M + 3.4, y + 34, 50, 6, "Mi compañero/a de apoyo:", 8.6, NEGRO, TXT)
    linea(sl, M + 42, y + 39, M + 140, y + 39)
    caja_texto(sl, M + 142, y + 34.5, 50, 6, "alguien de confianza, con su nombre", 7.4, GRIS, TXT)
    for k, t in enumerate(("Mi firma", "Firma de mi compañero/a: «te acompaño estos 21 días»")):
        x = M + 3.4 + k * ((A - 6.8) / 2 + 3)
        linea(sl, x, y + 47, x + (A - 6.8) / 2 - 3, y + 47, NEGRO, 0.8)
        caja_texto(sl, x, y + 47.6, (A - 6.8) / 2, 4, t, 7.4, RGBColor(0x33, 0x33, 0x33), TXT)
    y = 163
    caja(sl, M, y, A, 72)
    etiqueta(sl, M + 3.4, y + 2.4, "", "Mis 21 días",
             "marca la casilla cada día que cumplas · escribir este mapa ya es el día 1", tam=13)
    celda = (A - 6.8 - 14 - 6 * 1.8) / 7
    for s in range(3):
        yy = y + 10 + s * 16.3
        caja_texto(sl, M + 3.4, yy + 5, 14, 6, f"Semana {s + 1}", 7.8, NEGRO, TIT, negrita=True, mayus=True)
        for d in range(7):
            n = s * 7 + d + 1
            x = M + 3.4 + 14 + d * (celda + 1.8)
            c = rect(sl, x, yy, celda, 14.5, relleno=RGBColor(0xE6, 0xE6, 0xE6) if n == 21 else None,
                     borde=NEGRO, grosor=2 if n == 1 else 1, forma=MSO_SHAPE.ROUNDED_RECTANGLE, radio=0.12)
            del c
            caja_texto(sl, x + 1.3, yy + 0.6, 8, 4, str(n), 7.4, NEGRO, TXT, negrita=True)
            extra = "hoy" if n == 1 else ("cuéntale a tu compañero/a" if n in (7, 14, 21) else "")
            if extra:
                caja_texto(sl, x + 1.2, yy + 9, celda - 2.2, 5, extra, 5.6 if n != 1 else 6.4, NEGRO, TXT,
                           negrita=n == 1, alinear=PP_ALIGN.RIGHT if n == 1 else None)
    caja_texto(sl, M + 3.4, y + 61, 50, 6, "Cuando lo logre, voy a:", 10.5, NEGRO, TIT, negrita=True)
    linea(sl, M + 46, y + 67, M + 128, y + 67)
    caja_texto(sl, M + 130, y + 62.5, 62, 6, "mi premio: algo que me ilusione y esté a mi alcance", 7.4, GRIS, TXT)
    caja_texto(sl, M, 238, A, 6, "Si fallas un día, el siguiente vuelves. Lo que no se vale es fallar dos seguidos.",
               10.5, NEGRO, TIT, negrita=True, alinear=PP_ALIGN.CENTER)
    caja_texto(sl, M, 246, 90, 5, "Pégalo hoy en tu cuarto, donde lo veas al levantarte.", 6.8, GRIS, TXT)
    caja_texto(sl, M + 70, 246, A - 70, 5, CREDITO, 6.2, GRIS, TXT, alinear=PP_ALIGN.RIGHT)
    nota(sl, NOTA_CREDITO)

    sl = prs.slides.add_slide(vacia)
    fondo(sl, BLANCO)
    cabecera(sl, "Mi trabajo <b>de hoy</b>", "Esta cara es tuya.\nNadie la va a leer.", M, A)
    caja_texto(sl, M, 28, A, 7, "", 13, NEGRO)
    etiqueta(sl, M, 28, "", "Dónde estoy y quién soy", "cuéntalo como es, no como debería ser", tam=13)
    y = 36
    for n, t in (("A", "Un día normal mío es…"), ("B", "Soy bueno o buena en… y me cuesta…"), ("C", "Me gustaría probar…")):
        caja(sl, M, y, A, 40)
        etiqueta(sl, M + 3.4, y + 2.4, n, t, "puedes escribir, dibujar o poner una palabra")
        renglones(sl, M + 3.4, y + 7, A - 6.8, 3, 10)
        y += 43
    y += 2
    caja(sl, M, y, A, 56)
    etiqueta(sl, M + 3.4, y + 2.4, "", "Tres cosas que quiero mejorar",
             "encierra en el círculo la que vas a trabajar 21 días", tam=13)
    caja_texto(sl, M + 3.4, y + 9, A - 6.8, 6, "Pueden ser de cualquier área: " +
               " · ".join(a.lower() for a in g.AREAS) + ".", 7.4, RGBColor(0x44, 0x44, 0x44), TXT)
    for k in range(3):
        yy = y + 16 + k * 13
        rect(sl, M + 3.4, yy + 5.5, 6.5, 6.5, borde=NEGRO, forma=MSO_SHAPE.OVAL)
        linea(sl, M + 12.4, yy + 12, M + A - 3.4, yy + 12)
    caja_texto(sl, M, y + 60, 110, 5, "Ahora voltea la hoja: la cara del frente es la que va en la pared.", 6.8, GRIS, TXT)
    caja_texto(sl, M + 90, y + 60, A - 90, 5, CREDITO, 6.2, GRIS, TXT, alinear=PP_ALIGN.RIGHT)
    pie_logos_mapa(sl, M, A)
    nota(sl, NOTA_CREDITO)
    oculta(lamina_creditos(prs, W, H, True))
    prs.save(SALIDA / "MAPA-21-DIAS-carta.pptx")


def pie_logos_mapa(sl, M, A):
    y = 255
    cx = M
    for ruta, alto in ((L_ENLATA, 6), (L_IAVANZA, 4.4), (L_AMDV, 12)):
        pic = sl.shapes.add_picture(str(ruta), Mm(cx), Mm(y + 6 - alto / 2), height=Mm(alto))
        cx += pic.width / 36000 + 5


# ---------------------------------------------------------------- Word: manual y plantillas

def referencia():
    ref = SALIDA / "_referencia.docx"
    datos = subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                           capture_output=True, check=True).stdout
    ref.write_bytes(datos)
    doc = Document(ref)
    st = {s.name: s for s in doc.styles}
    for nombre in ("Normal", "Body Text", "First Paragraph", "Compact"):
        if nombre in st:
            st[nombre].font.name = TXT
            st[nombre].font.size = DPt(10)
    colores = {"Heading 1": (g.TINTA, 22), "Heading 2": (g.NARANJA, 15), "Heading 3": (g.TINTA, 12),
               "Title": (g.TINTA, 26), "Subtitle": (g.NARANJA, 14)}
    for nombre, (color, tam) in colores.items():
        if nombre in st:
            s = st[nombre]
            s.font.name = TIT
            s.font.size = DPt(tam)
            s.font.bold = nombre in ("Heading 3",)
            s.font.color.rgb = DRGB.from_string(color[1:])
            s.font.all_caps = nombre in ("Heading 1", "Heading 2", "Title")
    sec = doc.sections[0]
    sec.page_width, sec.page_height = DMm(215.9), DMm(279.4)
    for lado in ("left_margin", "right_margin"):
        setattr(sec, lado, DMm(18))
    sec.top_margin, sec.bottom_margin = DMm(30), DMm(20)
    cab = sec.header.paragraphs[0]
    cab.text = ""
    for ruta, alto in ((L_ENLATA, 8), (L_IAVANZA, 5.8), (L_AMDV, 15)):
        cab.add_run().add_picture(str(ruta), height=DMm(alto))
        cab.add_run("      ")
    pie = sec.footer.paragraphs[0]
    pie.text = ""
    pie.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = pie.add_run(CREDITO)
    r.font.size, r.font.name = DPt(7), TXT
    r.font.color.rgb = DRGB(0x77, 0x77, 0x77)
    doc.save(ref)
    return ref


def docx(md, destino, ref):
    subprocess.run(["pandoc", str(md), "-f", "gfm", "-t", "docx", "--reference-doc", str(ref), "-o", str(destino)],
                   check=True)


def main():
    SALIDA.mkdir(exist_ok=True)
    for viejo in list(SALIDA.glob("*.pptx")) + list(SALIDA.glob("*.docx")):
        viejo.unlink()
    presentacion()
    laminas()
    mapa()
    ref = referencia()
    docx(PAQ / "MANUAL-METODOLOGICO.md", SALIDA / "MANUAL-METODOLOGICO.docx", ref)
    for md in sorted((PAQ / "plantillas").glob("*.md")):
        docx(md, SALIDA / f"{md.stem}.docx", ref)
    ref.unlink()
    for p in sorted(SALIDA.iterdir()):
        print(p)


if __name__ == "__main__":
    main()
