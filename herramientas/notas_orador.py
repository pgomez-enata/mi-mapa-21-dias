"""Notas del orador de la presentación del aula, lámina por lámina.

Las usan generar_editables.py (al crear PRESENTACION-AULA-16x9.pptx) y la página de facilitadores
del Tour. Salen del manual del facilitador v4 (30-oct-2026): si cambia el guion, se cambia aquí.
"""

LAMINAS = [
    {
        "n": 0, "titulo": "Quién soy (tu lámina)", "minutos": "Antes del 00 · 30 segundos", "bloque": "Presentación del facilitador",
        "estudiante": "Sabe quién le habla y por qué.",
        "dices": "Buenos días. Yo soy ___. Me dedico a ___. Algo que empecé y terminé: ___. Algo en lo que fallé: ___.",
        "ojo": "Máximo 30 segundos. Sin teléfono, correo, redes, precios, logos de tu empresa ni códigos QR. Contar a qué te dedicas no es vender.",
    },
    {
        "n": 1, "titulo": "Bienvenida · Emprender no siempre es un negocio", "minutos": "00 – 04", "bloque": "Apertura",
        "estudiante": "Se levanta, se ríe y entiende de qué va.",
        "dices": "Levántese el que piense que emprender es montar un negocio. (Quédense de pie.) Ahora siéntese el que alguna vez decidió mejorar algo de su vida sin que nadie se lo pidiera. Eso es emprender. Hoy cada uno sale con un mapa de 21 días para pegar en su cuarto. Una sola regla: lo que escriban es de ustedes; nadie va a leer lo de otro.",
        "ojo": "La Semana Global de Emprendimiento se celebra en más de 180 países, y en República Dominicana desde hace 13 años.",
    },
    {
        "n": 2, "titulo": "Bloque 1 · Dónde estoy y quién soy", "minutos": "04 – 14", "bloque": "Dónde estoy y quién soy",
        "estudiante": "Llena las 3 líneas de la cara «Mi trabajo de hoy» y le cuenta una a su pareja.",
        "dices": "Tres líneas. Puedes escribir, dibujar o poner una sola palabra: un día normal mío es…; soy bueno o buena en… y me cuesta…; me gustaría probar… Si se quedan quietos: ¿para qué te buscan tus amigos?",
        "ojo": "Minuto 11 al 13: en parejas, una sola línea, un minuto cada uno; el cambio se marca con una palmada. Cierra con: nadie arranca de cero, arranca de donde está.",
    },
    {
        "n": 3, "titulo": "Bloque 2 · Tres cosas que quiero mejorar", "minutos": "14 – 19", "bloque": "Tres cosas y escojo una",
        "estudiante": "Escribe tres cosas y encierra una.",
        "dices": "¿Qué te molesta? ¿De qué te quejas? Quéjense un minuto, en voz alta. Ahí está lo que pueden mejorar. Pon tres cosas de tu vida de hoy y encierra una: no la más grande, la que de verdad quieres.",
        "ojo": "Para destrabar: dormir más temprano, pasar Matemática, pelear menos con mi hermano, ahorrar para unos tenis. Mano alzada por área, rápido; no se cuenta.",
    },
    {
        "n": 4, "titulo": "Bloque 3 · Mi mapa de 21 días", "minutos": "19 – 33", "bloque": "Mi mapa (cajas 1, 2 y 3)",
        "estudiante": "Voltea la hoja y llena las cajas 1, 2 y 3 mientras tú llenas la tuya en grande.",
        "dices": "Caja 1: una frase que se pueda ver («voy a dormir antes de las 11», no «quiero ser mejor»). Caja 2: de pie, tres respiraciones lentas, ojos cerrados: es el día 21, ¿qué cambió? Caja 3: tu historia en 2 minutos y luego «¿qué de ti o de tu día puede hacer que lo dejes?».",
        "ojo": "Es la lámina que más tiempo queda en pantalla. Pasea entre las filas y arregla en voz alta 2 o 3 frases vagas, sin decir de quién son.",
    },
    {
        "n": 5, "titulo": "Bloque 3 · Si pasa…, entonces…", "minutos": "33 – 42", "bloque": "Mi mapa (caja 4, compañero, premio y firma)",
        "estudiante": "Escribe su plan, escoge compañero/a de apoyo, su premio, firma y marca el día 1.",
        "dices": "Cuando ___, voy a ___: algo pequeño y con hora. Y abajo: si pasa lo de tu caja 3, entonces tú ___. Escojan a su compañero/a de apoyo. Escribe tu premio: algo que te ilusione y esté a tu alcance. Léelo, firma, y que tu compañero/a firme al lado. Marquen el día 1.",
        "ojo": "La regla: si fallas un día, el siguiente vuelves; lo que no se vale es fallar dos seguidos. Del 42 al 45 va el patrocinador si lo hay; si no, ese tiempo es para terminar el mapa.",
    },
    {
        "n": 6, "titulo": "Cierre · Pégalo hoy", "minutos": "45 – 50", "bloque": "Cierre",
        "estudiante": "Entrega la tarjeta de salida (si el kit la trae) y dice en voz alta la primera palabra de lo que va a mejorar.",
        "dices": "A la cuenta de tres, cada uno dice la primera palabra de lo que va a mejorar. El mapa va pegado hoy mismo en tu cuarto, donde lo veas al levantarte. 21 días es el primer tramo: si llegas, ya no eres el mismo que empezó hoy. Esto es emprender. Gracias.",
        "ojo": "Después: el voluntario cierra el sobre y toma la foto de la lista; tú le entregas al orientador la nota de seguimiento de los días 7, 14 y 21.",
    },
]


def texto_nota(i: int) -> str:
    d = LAMINAS[i]
    return (f"{d['minutos']} · {d['bloque']}\n\nQué hace el estudiante: {d['estudiante']}\n\n"
            f"Qué dices: «{d['dices']}»\n\nOjo: {d['ojo']}")
