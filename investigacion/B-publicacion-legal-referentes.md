# B · Publicación abierta, marco legal RD y referentes
**Taller «Mi mapa de 21 días»** · Fundación Enlata · IAvanza · Fundación Ayudar Me Da Vida · GEW RD 2026
Investigación al 30-oct-2026. Cada dato lleva su fuente (ver lista al final). Lo que no se pudo verificar está marcado **[sin verificar]**.
*Esto no es asesoría legal; antes de publicar o firmar acuerdos con escuelas conviene que un abogado dominicano lo revise.*

---

## A. Publicar la metodología como recurso abierto

### A1. ¿Qué licencia usar?

| Licencia | Qué permite | Qué exige | ¿Es «abierta»? (Open Definition / UNESCO REA 2019) | Pros y contras para «Mi mapa de 21 días» |
|---|---|---|---|---|
| **CC BY 4.0** | Copiar, adaptar y usar con cualquier fin, también comercial | Dar crédito e indicar si se hicieron cambios | **Sí.** Cumple la Open Definition y es REA según UNESCO | La más fácil de reutilizar (MINERD, ONG, universidades). Riesgo: alguien puede adaptarla y cerrar su versión |
| **CC BY-SA 4.0** | Lo mismo, también con fines comerciales | Crédito más *compartir igual*: las versiones derivadas deben salir con la misma licencia | **Sí.** Cumple la Open Definition (permite exigir *share-alike*) | Mantiene abiertas las mejoras. Es la que usa Wikipedia y la que adoptó **Liberating Structures en junio de 2026**, cuando quitó la cláusula NC. Contra: no se puede mezclar con material NC o ND |
| **CC BY-NC-SA 4.0** | Adaptar y compartir solo sin fines comerciales | Crédito, sin uso comercial y compartir igual | **No para la Open Definition** (el NC discrimina «campos de actividad»). UNESCO exige acceso sin costo, reutilización, adaptación y redistribución, y no prohíbe el NC de forma expresa. En la práctica sí se cuenta como REA (OER Commons lo admite) | Es la del d.school de Stanford. Contra: «comercial» es ambiguo (¿un colegio privado?, ¿un consultor que cobra por facilitar?) y frena la adopción. Liberating Structures la abandonó por eso: «frenaba la adaptación creativa» |

**Por qué lo dice cada fuente:**
- Open Definition, sección «Non-Conformant Licenses»: las CC NonCommercial «no respetan la cláusula de no discriminar campos de actividad»; las CC NoDerivs violan la cláusula de reutilización.
- Recomendación UNESCO sobre REA (2019): los REA son materiales de dominio público o con licencia abierta «que permiten el acceso sin costo, la reutilización, la reorientación, la adaptación y la redistribución por terceros».

**Recomendación: un paquete de cuatro piezas**
1. **Contenido (manual, guiones, fichas, plantillas): CC BY-SA 4.0.** Encaja con «psicología abierta»: cualquiera puede usarlo y mejorarlo, y las mejoras siguen abiertas. Si se busca máxima adopción institucional (por ejemplo, que MINERD lo integre a sus propios materiales), CC BY 4.0 es la alternativa.
2. **Código (scripts, generadores de PDF, formulario de seguimiento): MIT** si se quiere máxima reutilización, o **GPL-3.0** si se quiere copyleft como en el contenido. Con CC BY-SA en el contenido, lo coherente es GPL-3.0. Si el código es pequeño, MIT es más simple.
3. **Nombre y logo** («Mi mapa de 21 días», Enlata, IAvanza, Ayudar Me Da Vida, Manchis): **fuera de la licencia.** Se protegen con una *política de marca*.
4. **«Facilitador certificado»**: un **programa de certificación** aparte de la licencia.

### A2. ¿La licencia puede exigir «tomar la formación antes de replicar»? **No.**

- La licencia CC 4.0, sección 2(a)(5)(C) «No downstream restrictions», prohíbe imponer condiciones adicionales. La sección 3(b)(3) de BY-SA impide añadir términos extra a las adaptaciones. Si se añade «solo tras la formación», la licencia deja de ser CC, deja de ser abierta y genera confusión jurídica.
- La propia licencia ofrece la salida. En la sección 2(b)(2), **«los derechos de patente y de marca no se licencian»**, y la sección 2(a)(6) dice que la licencia no implica aval («No endorsement»).

**Cómo hacerlo bien:**

| Pieza | Qué dice | Dónde |
|---|---|---|
| Licencia de contenido | «Puedes usar, adaptar y compartir este manual (CC BY-SA 4.0)» | `LICENSE` |
| Política de marca y nombre | «El nombre "Mi mapa de 21 días", los logos y la frase "taller oficial" solo los usan facilitadores certificados por las fundaciones. Si adaptas el material sin certificación, llámalo distinto o di "adaptado de…" y no uses los logos» | `MARCA.md` |
| Certificación de facilitadores | Formación oficial más práctica supervisada más compromiso de salvaguarda. Da derecho a decir «facilitador certificado» y a figurar en el directorio | `CERTIFICACION.md` y web |
| Recomendación (no obligación) | «Si eres docente, te pedimos tomar la formación oficial: el taller trabaja con adolescentes y toca metas personales. La formación incluye el protocolo de protección (salvaguarda) y de denuncia» | Portada del manual y README |
| Aviso de no aval | «Las adaptaciones no están avaladas por las fundaciones salvo que lo indiquemos por escrito» | README y pie del PDF |

Para que la marca valga contra terceros conviene registrarla. En RD el registro de marcas lo lleva **ONAPI** (Oficina Nacional de la Propiedad Industrial) **[procedimiento y costo sin verificar en esta ronda]**.

### A3. Dónde y cómo publicar

**Pila recomendada:**

| Capa | Herramienta | Para qué |
|---|---|---|
| Fuente editable | Repositorio **GitHub** público (Markdown como fuente y ODT/DOCX exportados) | Control de versiones, aportes, *issues* |
| Versiones | **SemVer** (`v1.0.0` = primera edición validada; `1.1.0` = sección nueva; `1.0.1` = erratas) y `CHANGELOG.md` en formato *Keep a Changelog* | Saber qué cambió y cuándo |
| DOI citable | **Zenodo** conectado a GitHub. Cada *release* archiva y emite un DOI por versión, más un *concept DOI* que apunta siempre a la última | Citación académica, preservación a largo plazo (CERN) |
| Citación | `CITATION.cff` en la raíz. GitHub muestra «Cite this repository» y Zenodo importa los metadatos | Autores, ORCID, versión, licencia |
| Web legible | **GitHub Pages** (o la web de Enlata) que genere HTML y PDF desde el Markdown | Lectura en celular y descarga |
| Repositorios REA | **OER Commons** (ficha que enlaza a Zenodo/GitHub) e **Internet Archive** (espejo del PDF) | Descubribilidad docente y copia redundante |
| Descargables | PDF imprimible más ODT editable más fichas A4 en blanco y negro | Escuelas sin internet o sin impresora a color |

**Estructura del repositorio:**
```
mi-mapa-21-dias/
├── README.md            # qué es, para quién, cómo usarlo, aviso de salvaguarda, licencia en 3 líneas
├── LICENSE              # CC BY-SA 4.0 (contenido)
├── LICENSE-CODE         # MIT o GPL-3.0 (carpeta /herramientas)
├── MARCA.md             # política de nombre y logos
├── CERTIFICACION.md     # cómo ser facilitador certificado
├── SALVAGUARDA.md       # protocolo de protección y ruta de denuncia (resumen de la sección B)
├── CITATION.cff
├── CHANGELOG.md
├── CONTRIBUTING.md      # cómo proponer cambios; todo aporte se licencia CC BY-SA
├── CREDITOS.md          # métodos de terceros y sus términos (ver A4)
├── manual/              # capítulos .md
├── fichas/              # mapa de 4 casillas, ficha de compañero, check-ins 7/14/21
├── formacion/           # guion de la formación de facilitadores
├── herramientas/        # scripts (generar PDF, etc.)
└── traducciones/
```

**Ejemplos de manuales metodológicos abiertos y su licencia:**

| Ejemplo | Licencia verificada | Lección |
|---|---|---|
| **Design Thinking Bootleg** (Stanford d.school, 2018) | **CC BY-NC-SA 4.0** (el *Bootcamp Bootleg* de 2010 era CC BY-NC-SA 3.0) | Formato baraja/fichas; créditos detallados por autor |
| **Field Guide to Human-Centered Design** (IDEO.org, 2015) | **CC BY-NC-ND 3.0**: no permite derivados, así que **no es REA** | Contraejemplo: es gratis pero no abierto, porque no se puede adaptar |
| **Liberating Structures** | **CC BY-SA 4.0 desde junio de 2026** (antes BY-NC-SA). El material anterior a esa fecha puede seguir con NC | Mejor modelo: licencia abierta más un **«núcleo estable»** (principios, íconos, pasos mínimos) que piden no alterar, y comunidad de práctica. Ofrecen textos de atribución listos para copiar |
| **Hyper Island Toolbox** | **No es abierto**: acceso gratuito previo registro; «todos los métodos © de sus respectivos dueños» | Muestra el riesgo de recopilar métodos ajenos sin licencia clara |
| **Lean In Girls** | **No es CC**: currículo gratis con registro y «Términos de uso» propios (uso solo para la misión, revocable) | Gratis no es lo mismo que abierto |
| **Character Lab — WOOP for Classrooms** | Gratis para docentes, sin licencia CC encontrada **[sin verificar]**. **Character Lab cerró operaciones en junio de 2024**; su web es un archivo | Si el material depende de una sola organización, puede desaparecer. Zenodo e Internet Archive mitigan ese riesgo |

### A4. Métodos de terceros dentro de un manual CC (caso WOOP)

**Lo verificado:** WOOP (Wish-Outcome-Obstacle-Plan) es de Gabriele Oettingen. En la literatura se llama *Mental Contrasting with Implementation Intentions* (MCII): Oettingen junto con las intenciones de implementación de Peter Gollwitzer. Los materiales oficiales llevan «© Gabriele Oettingen». Un programa de terceros declara: «Gabriele Oettingen owns the copyright and registered trademark for WOOP; used with permission».

**Reglas prácticas:**
1. **Las ideas no tienen derechos de autor; la expresión sí, y el nombre puede ser marca.** Se puede enseñar el *principio* (contrastar el deseo con el obstáculo interno y hacer un plan «si… entonces…») con texto, ejemplos y fichas propias.
2. **No relicenciar lo ajeno.** No copiar hojas, guiones ni textos de woopmylife.org ni de Character Lab dentro del manual CC BY-SA. Lo que no es propio se *enlaza*, no se incrusta.
3. **No usar «WOOP» como nombre del taller ni de las casillas** sin permiso. Lo seguro es usar nombres propios (por ejemplo «Mi deseo · Mi mejor resultado · Mi obstáculo · Mi plan si… entonces…») y escribir aparte: «Inspirado en la estrategia WOOP/MCII de Gabriele Oettingen y Peter Gollwitzer. WOOP es marca de G. Oettingen; este material no está afiliado ni avalado por ella. Más en woopmylife.org». Si se quiere usar el nombre WOOP, pedir permiso por escrito por el contacto de woopmylife.org.
4. **Marcar las excepciones en la licencia:** «Salvo indicación en contrario, este manual está bajo CC BY-SA 4.0. Las marcas, logos y los métodos citados en `CREDITOS.md` pertenecen a sus dueños y no se licencian aquí».
5. **Atribución tipo TASL** (Título, Autor, Fuente, Licencia) para todo material CC de terceros que sí se incorpore. Si se adaptan estructuras de Liberating Structures (por ejemplo 1-2-4-Todos), usar su texto de atribución, que ya es compatible con BY-SA.
6. **Citar la evidencia, no exagerarla:** referenciar los estudios de Oettingen y Gollwitzer sin prometer resultados a los estudiantes.

---

## B. Marco legal dominicano para trabajar con menores en escuelas

### B4. Ley 136-03 (Código para el Sistema de Protección y los Derechos Fundamentales de NNA)

| Art. | Qué dice (texto verificado en el PDF oficial) | Implicación para el taller |
|---|---|---|
| **14 — Deber de denunciar** | «Los profesionales y funcionarios de las áreas de la salud, pedagogía, sicología, trabajo social y agentes del orden público, directores y funcionarios, tanto públicos como privados, **y cualquier otra persona** que en el desempeño o no de sus funciones tuviere **conocimiento o sospecha** de una situación de abuso o de violación de los derechos de los NNA, **están obligados a denunciarla** ante las autoridades competentes, estando **exentos de responsabilidad penal y civil** con respecto a la información que proporcionen». Párrafo: el incumplimiento se sanciona con **1 a 3 salarios mínimos** (Sala Penal del Tribunal de NNA) | **Todo facilitador voluntario está obligado a denunciar**, y con basta la *sospecha*. No puede prometer confidencialidad absoluta a un estudiante |
| **18 — Intimidad** | Derecho al honor, la reputación, la imagen propia, la vida privada y la intimidad | Las fichas del «mapa» son personales: no se recogen ni se exhiben sin permiso del estudiante |
| **26 — Protección de la imagen** | Prohíbe «disponer o divulgar, a través de cualquier medio, la imagen y datos de los NNA» de forma que afecte su desarrollo, honor o reputación, o que constituya injerencia en su vida privada o pueda estigmatizarlos. Se sanciona según el art. 411 | Fotos y videos con consentimiento, sin nombres y sin datos sensibles (ver B8) |
| **49 / 50** | Derecho a ser respetados por los educadores. MINERD, por Orientación y Psicología, establece los mecanismos de denuncia en centros, distritos y regionales | Coordinarse con el **orientador o psicólogo del centro** como primer enlace interno |
| **238 / 256** | Cualquiera puede denunciar ante el **Ministerio Público de NNA**, que tiene la acción pública | Destino formal de la denuncia penal |
| **474** | Si la junta local de protección encuentra indicios de abuso físico, psicológico o sexual, remite la denuncia de inmediato al Ministerio Público | El sistema CONANI y Ministerio Público está conectado |

**Ruta de denuncia (canales oficiales que difunde CONANI):** **Línea Vida 809-200-1202** (24 h, gratis, puede ser anónima; la Procuraduría asigna fiscal) · **Sistema 9-1-1** · **Procuraduría Fiscal de NNA (809-596-4951)** · oficinas municipales y regionales de CONANI. En la escuela, además: informar a la dirección y a Orientación y Psicología, según las Normas de Convivencia (abajo). Para apoyo emocional no urgente: Centro de Contacto «Cuida tu Salud Mental» (809) 200-1400.

**Estado de reforma:** CONANI informó (19-ago-2026) que la propuesta de reforma de la Ley 136-03 **sigue en borrador**. La ley vigente es la del 2003.

### B5. Ley 172-13 de protección de datos personales

- **Art. 5 (num. 4) — Consentimiento:** el tratamiento es ilícito si el titular no dio consentimiento **«libre, expreso y consciente», por escrito** o por un medio equiparable, previa información de la finalidad.
- **Art. 6 (num. 7) — Definición:** manifestación de voluntad «libre, inequívoca, específica e informada».
- **Art. 79 — Datos de menores:** su tratamiento «estará normado por las disposiciones establecidas en el **Código para la Protección de los Derechos de los NNA** [Ley 136-03], el Código Penal y otras leyes especiales». La 172-13 **no fija una edad** para que el menor consienta solo; remite a la 136-03. *(En otros países hay umbrales, como 14 años en España, pero no aplican en RD.)*
- **Art. 76:** los datos sobre opiniones, convicciones, salud o vida sexual exigen consentimiento **expreso y por escrito**. Las metas personales pueden tocar salud o creencias.

**Práctica recomendada** (deducida de la norma; no la exige ningún artículo concreto): para guardar datos personales de un menor (nombre, teléfono o correo para los *check-ins* de los días 7, 14 y 21, fotos), pedir **autorización escrita del padre, madre o tutor** (gestionada por la escuela) y además el **asentimiento del adolescente**. Recoger lo mínimo. No pedir el contenido de la meta. Borrar los datos al cerrar el ciclo de 21 días. Hacer los *check-ins* dentro del aula con el docente, no por WhatsApp privado entre adulto voluntario y menor.

### B6. Normas de MINERD

| Instrumento | Año | Qué aporta |
|---|---|---|
| **Normas del Sistema Educativo Dominicano para la Convivencia Armoniosa en los Centros Educativos Públicos y Privados** (MINERD y CONANI, con apoyo de UNICEF; aprobadas por el Consejo Nacional de Educación, en cumplimiento de los arts. 48-49 de la Ley 136-03) | 2.ª ed. **julio de 2013** | **Art. 11 «Obligación de denunciar»**: directivos, docentes, personal administrativo «y cualquier otra persona» que tenga conocimiento o sospecha de abuso, **«sea o no en el ámbito del centro educativo»**, debe denunciar (remite al art. 14 de la Ley 136-03). Arts. 40-44: el centro está obligado a recibir denuncias, llevar un libro de registro, y Orientación y Psicología define los protocolos |
| **Consejo Nacional de Educación — actualización de políticas y protocolos contra la violencia de género, intrafamiliar y sexual** | Aprobado el **30-jul-2026** | Herramientas estandarizadas de detección, capacitación obligatoria, sello ministerial para centros que cumplan, canales directos con Ministerio de la Mujer, Interior y Policía, Ministerio Público, Policía Nacional y CONANI, y norma de confidencialidad para evitar la revictimización. **El documento final no se encontró publicado** |
| **Protocolo escolar ante sospecha de consumo o tenencia de sustancias psicoactivas** (MINERD con el Consejo Nacional de Drogas) | 26-jun-2025 | Referencia de la ruta 911, CAINNACSP y Policía Escolar |
| «Protocolo de prevención, detección y atención de la violencia en centros educativos» (nombre exacto que se pidió verificar) | — | **[sin verificar]**: no se encontró un documento oficial de MINERD con ese título exacto. Lo vigente y verificable son las Normas de Convivencia (2013) y la actualización del CNE (2026). **Recomendación:** que cada escuela anfitriona entregue por escrito su protocolo y el nombre de su orientador antes del taller |

**Actividades externas en escuelas:** no se encontró una ordenanza específica de MINERD sobre ONG o voluntarios externos dando talleres **[sin verificar]**. En la práctica se coordina con la dirección del centro y el distrito. Conviene una carta de acuerdo con la escuela que cubra fecha, presencia de un docente del centro en el aula, uso de imagen y ruta de denuncia.

### B7. Nuevo Código Penal: Ley 74-25

- **Promulgada el 3-ago-2025** y publicada en la Gaceta Oficial n.º 11208 el 5-ago-2025. Sustituye el Código de 1884.
- **Vigencia:** 12 meses de *vacatio legis* (art. 393). Hubo debate entre **3-ago-2026** (Subero Isa, consultor jurídico del Poder Ejecutivo) y **5-ago-2026** (Ministerio Público). La **Ley 44-26** (modificaciones) entra en vigor junto con la 74-25. **Ya está vigente en ambos casos.**
- **Responsabilidad penal de personas jurídicas (arts. 8-11):** aplazada al **5-nov-2026** por la Ley 44-26. Esto **alcanza a fundaciones y asociaciones**, que responden por fallas de dirección, control y supervisión de sus órganos o subordinados. Es una razón más para tener una política de salvaguarda escrita y supervisada.
- **Relevante para menores** (según fuentes secundarias de despachos y prensa; contrastar con el texto oficial): tipifica el **acoso escolar (bullying) y el ciberacoso**; amplía a **30 años, contados desde la mayoría de edad de la víctima**, la prescripción de ciertos delitos sexuales contra menores; endurece el abandono de menores (hasta 10 años); y crea el delito de **denuncia falsa** (hasta 2 años).
- **No se encontró** en la 74-25 un tipo nuevo de «omisión de denunciar abuso infantil». El deber de denunciar sigue en el **art. 14 de la Ley 136-03** **[confirmar con el texto íntegro]**.

### B8. Estándares internacionales de salvaguarda

| Estándar o práctica | Fuente | Aplicación |
|---|---|---|
| **Keeping Children Safe — International Child Safeguarding Standards**: 4 estándares, **Política, Personas, Procedimientos, Rendición de cuentas** | Keeping Children Safe (guía de 2014) | Política firmada por las tres fundaciones. Código de conducta que firma cada facilitador. Ruta de denuncia interna con responsable designado (*focal point*). Revisión anual |
| **Regla de dos adultos** (nunca un adulto a solas con un menor; siempre a la vista) | Práctica estándar de salvaguarda (KCS «Personas/Procedimientos»; Scouting usa «two-deep leadership») **[fuente específica sin verificar en esta ronda]** | Siempre dos facilitadores, o un facilitador más el docente del centro. Ninguna conversación a solas fuera de la vista. Sin contacto privado por redes o WhatsApp con estudiantes |
| **Política de fotos** | Práctica usual de ONG de infancia (UNICEF, Save the Children); el sustento legal en RD está en los arts. 18 y 26 de la Ley 136-03 | Solo con autorización escrita del tutor. Por defecto, tomas de **espaldas, manos, fichas sin nombres o planos generales a distancia**. Nunca nombre más escuela más cara juntos. Nunca el contenido del «mapa» personal. Respetar el «no» del adolescente aunque haya permiso del tutor. Encaja con la regla interna ya vigente de que los insertos no tapen caras y con la de contenido público sin aval institucional |
| **Selección de voluntarios** | KCS «Personas» | Entrevista, referencias y, cuando sea posible, **certificado de no antecedentes penales** (Procuraduría General) **[trámite sin verificar en esta ronda]** |

---

## C. Referentes comparables

| Programa | Formato y duración | Seguimiento | Formación de facilitadores | ¿Material abierto? Licencia |
|---|---|---|---|---|
| **JA Dominicana** (desde 1995; afiliada a JA Worldwide) | Simuladores por equipos para bachillerato: **SIEMPRE** (empresa de manufactura), **Banquero Joven Popular**, **Viviendo Seguro**; también Aula Virtual. Dice tener más de 20,500 jóvenes y más de 300 voluntarios | Competencias entre equipos | Voluntarios del sector empresarial (modelo JA: voluntario corporativo en el aula) | **No.** Web: «© Derechos reservados» |
| **Character Lab — WOOP Playbook** (EE. UU.) | Actividad escrita de unos minutos, en aula, tutoría o asamblea, con video de 1 min; hay traducciones (también al español) | Repetir WOOP con frecuencia (recomendación de Oettingen) | Docentes, en cumbres y *workshops* con la propia Oettingen; recursos en línea | Gratis; licencia abierta **[sin verificar]**. **Cerró en junio de 2024** |
| **Lean In Girls** | **15 sesiones de 1 h**, de 11 a 15 años, en grupos pequeños | Programa de varias semanas | Manual del facilitador más **formación opcional gratuita** | Gratis con registro; **términos propios, revocables, no CC** |
| **NFTE** (EE. UU., global) | **BizCamp: 50 a 90 h** intensivas en verano (grados 6 a 12), con concurso de *pitch* y capital semilla (p. ej. US$300) | Concurso y red de exalumnos; mide antes y después con el *Entrepreneurial Mindset Index* | **Docentes certificados** («NFTE University», *Entrepreneurial Teacher Corps*) | No abierto (currículo propietario). Costo de referencia en 2021: unos US$1,000 por estudiante |
| **UNICEF UPSHIFT** (nació en Kosovo; global) | Talleres de innovación social más **mentoría más capital semilla**, de 15 a 24 años. Algunas ediciones duran **5 meses** con *Demo Day* | Mentoría y mini-subvenciones | Guía de implementación y *toolkit* para facilitadores locales; insiste en adaptar al contexto | El *toolkit* circula; licencia **[sin verificar]**. Muchas publicaciones de UNICEF usan CC BY-NC-SA 3.0 IGO |
| **Peace First** | Reto de innovación social: unos 6 meses de talleres y *coaching*, con micro-subvenciones (p. ej. US$1,000) y *sprints* virtuales de 2 días | *Coaching* | Mentores y coaches | **[sin verificar]** |
| **Construye T** (SEP-SEMS México con PNUD; desde 2008) | Habilidades socioemocionales en bachillerato público: **12 lecciones de 20 min por semestre**, una por semana, integradas en las asignaturas. La dimensión «Elige T» incluye metas | Secuencia de 6 semestres | Capacitación a directivos y docentes dentro de la formación continua oficial; manual del maestro | Descarga pública en gob.mx y sitios escolares; licencia **[sin verificar]** |
| **Aflatoun** (Ámsterdam; más de 100 países) | Currículos por edad (Aflateen para 15 a 18 años; unas 40 h al año en primaria). Club estudiantil, ahorro, microempresa | Club continuo | **Franquicia social**: más de 300 socios contextualizan y aplican el currículo; formación de formadores | **No abierto**: acceso para socios por plataforma; adaptación local autorizada **[licencia sin verificar]** |

### Tres lecciones más útiles para «Mi mapa de 21 días»
1. **Brevedad repetida, más que un evento largo.** Construye T (20 min por semana) y Character Lab (WOOP en minutos, repetido) muestran que lo que se sostiene es el *ritual corto y recurrente*. Los *check-ins* de los días 7, 14 y 21 deben ser **ultracortos (5 a 10 min) y en manos del docente del centro**, no del voluntario, porque el voluntario no vuelve. Así el docente es el ancla, como en Construye T.
2. **Abierto más certificado más núcleo estable.** El modelo de Liberating Structures (CC BY-SA, con un «núcleo» de pasos e íconos que piden no alterar y una comunidad que comparte adaptaciones) y el de Lean In Girls y NFTE (formación de facilitadores aparte del material) responden a la frase de Piero: el contenido es libre y el sello de calidad es la certificación y la marca. Definir 4 o 5 **«especificaciones mínimas»** del taller (por ejemplo, las cuatro casillas en orden, el plan «si… entonces», la firma del compañero, la regla de dos adultos y los *check-ins*) que toda versión debe respetar para llamarse oficial.
3. **Que el material sobreviva a la organización y que la salvaguarda vaya incluida.** Character Lab cerró en 2024 y su material quedó en una web de archivo; Aflatoun e Hyper Island dependen de cuentas y registro. Publicar con DOI en Zenodo, más Internet Archive, más un repositorio abierto, garantiza la permanencia. Como todos los programas serios con menores separan la salvaguarda del contenido, el manual debe traer el **protocolo de denuncia (art. 14 de la Ley 136-03) como capítulo cero**, no como anexo.

---

## Referencias

**Licencias y apertura**
- Creative Commons, licencias: https://creativecommons.org/share-your-work/use-remix/cc-licenses
- CC BY-SA 4.0, texto legal (secciones 2(a)(5)(C), 2(a)(6), 2(b)(2), 3(b)): https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt
- Open Definition, licencias no conformes: https://opendefinition.org/licenses/nonconformant
- UNESCO, REA y Recomendación 2019: https://www.unesco.org/en/tags/open-educational-resources
- Liberating Structures, licencia CC BY-SA 4.0 (jun-2026): https://www.liberatingstructures.com/cc-license
- d.school, Design Thinking Bootleg (CC BY-NC-SA 4.0): https://dschool.stanford.edu/tools/design-thinking-bootleg
- d.school, Bootcamp Bootleg 2010 (CC BY-NC-SA 3.0): https://hpi.de/fileadmin/user_upload/fachgebiete/d-school/documents/01_GDTW-Files/bootcampbootleg2010.pdf
- IDEO.org, Field Guide (CC BY-NC-ND 3.0): https://openlab.citytech.cuny.edu/bassjrcomd3701fa2022/files/2021/02/Field-Guide-to-Human-Centered-Design_IDEO_lo.pdf
- Hyper Island Toolbox: https://hyperisland.com/en/toolbox-request-access · https://hyperisland.com/en/toolbox-of-the-month
- Lean In Girls, términos del currículo: http://leaningirls.org/curriculum · https://leanin.org/girls/girls-program

**Publicación**
- Zenodo y GitHub (DOI por versión y *concept DOI*): https://www.earthinversion.com/utilities/github-to-zenodo-code-data-doi · documentación oficial: https://help.zenodo.org/docs/github/
- GitHub, archivos CITATION: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
- SemVer: https://semver.org · Keep a Changelog: https://keepachangelog.com
- OER Commons: https://oercommons.org · Internet Archive: https://archive.org

**WOOP**
- WOOP my life (oficial): https://woopmylife.org/en/practice · https://woopmylife.org/en/science
- Ejemplo de aviso «Oettingen owns the copyright and registered trademark for WOOP; used with permission»: https://lyngblomsten.org/community-services/woop-groups
- Hoja oficial «© 2015-2016 Gabriele Oettingen»: https://static1.squarespace.com/static/5642d5eae4b0eadf5c6008bf/t/57b4695a893fc0bed59f6bdf/1471441243094/woop+exercise+written.pdf
- Character Lab, WOOP for Classrooms (sitio de archivo, cierre en jun-2024): https://characterlab.org/woop · resumen en español: https://characterlab.org/wp-content/uploads/2019/03/Character_Lab_WOOP_Spanish.pdf

**Marco legal RD**
- Ley 136-03, texto (OEA): http://www.oas.org/DIL/ESP/LEY%20136-03%20-%20Codigo%20para%20el%20Sistema%20de%20Protecci%C3%B3n%20y%20los%20Derechos%20Fundamentales%20de%20Ni%C3%B1os%20Ni%C3%B1as%20y%20Adolescentes%20Republica%20Dominicana.pdf
- Ley 136-03 (MINERD): https://www.ministeriodeeducacion.gob.do/docs/marco-legal/leyes/ley-que-crea-el-codigo-para-la-proteccion-de-ninos-ninas-y-adolescentes-no-136-03-go-no-10234-del-07-de-ago-del-2003.pdf
- CONANI, reforma de la 136-03 en borrador (ago-2026): https://conani.gob.do/conani-dice-propuesta-de-reforma-de-ley-136-03sigue-en-borrador-trabaja-en-integrar-recomendaciones-de-80-organizaciones
- CONANI, canales de denuncia y art. 14: https://conani.gob.do/conani-llama-a-proteccion-activa-de-ninos-ninas-y-adolescentes-pide-no-ignorar-senales-de-riesgo · https://conani.gob.do/conani-cierra-mes-de-la-prevencion-del-abuso-infantil-con-parada-artistica-reafirma-compromiso-con-proteccion-de-ninos-ninas-y-adolescentes
- Línea de salud mental (809) 200-1400: https://presidencia.gob.do/noticias/gana-y-conani-llaman-cuidar-la-salud-mental-y-proteger-de-la-violencia-ninos-ninas-y
- Ley 172-13 (ODAC): https://odac.gob.do/transparencia/index.php/marco-legal-de-transparencia/leyes?download=46%3Aley-172-13
- Normas de Convivencia Armoniosa (MINERD, 2013): https://ministeriodeeducacion.gob.do/docs/licitaciones-oai/hWl8-7-normas-de-convivencia-final-imprentapdf.pdf
- CNE aprueba actualizar protocolos (30-jul-2026): https://ministeriodeeducacion.gob.do/comunicaciones/noticias/consejo-nacional-de-educacion-aprueba-fortalecer-el-rol-de-las-escuelas-en-la-prevencion-de-la-violencia-de-genero-intrafamiliar-y-sexual
- Protocolo de sustancias (jun-2025): https://ministeriodeeducacion.gob.do/comunicaciones/noticias/minerd-y-consejo-nacional-de-drogas-refuerzan-prevencion-escolar-con-nuevo-protocolo-ante-consumo-de-sustancias
- Ley 74-25, entrada en vigor (Diario Libre, 3-ago-2026): https://www.diariolibre.com/actualidad/justicia/2026/08/03/codigo-penal-republica-dominicana-entra-en-vigor/3618551
- Ley 44-26, modificaciones y vigencia diferida de personas jurídicas (Pellerano & Herrera): https://phlaw.com/es/modificaciones-al-nuevo-codigo-penal-dominicano-ley-44-26 · https://phlaw.com/es/ley-44-26-principales-modificaciones-al-nuevo-codigo-penal-de-la-republica-dominicana
- Ley 74-25, resumen y bullying (Pellerano & Herrera): https://phlaw.com/es/codigo-penal-dominicano-ley-74-25 · PDF: https://phlaw.com/wp-content/uploads/2025/08/Ley-74-25-que-modifica-el-Co%CC%81digo-Penal-Dominicano-.pdf
- Prescripción de delitos sexuales contra menores (Barrigaverde): https://barrigaverde.net/nuevo-codigo-penal-entra-en-vigor-en-republica-dominicana-entre-expectativas-de-modernizacion-y-criticas-de-juristas-y-opositores

**Salvaguarda**
- Keeping Children Safe, estándares: https://www.keepingchildrensafe.global/international-child-safeguarding-standards
- Guía de implementación de 2014: https://resourcecentre.savethechildren.net/document/child-safeguarding-standards-and-how-implement-them

**Referentes**
- JA Dominicana: https://jadom.org · https://jadom.org/quienes-somos
- NFTE BizCamps: https://nfte.com/nfte-summer-bizcamps-empower-the-next-generation-of-innovators · https://nfte.com/events/miami-dade-tech-entrepreneurship-bizcamp
- UNICEF UPSHIFT: https://www.unicef.org/innovation/stories/upshift-20 · https://upshift4resilience.com/upshift-international-programme-applications-open
- Peace First: https://thesprout.co.uk/blog/peace-first-grant-opportunity · https://peacefirst.org/2026/01
- Construye T: https://www.gob.mx/sep/acciones-y-programas/programa-construye-t-4598 · https://www.undp.org/es/mexico/proyectos/construyet · https://www.gob.mx/cms/uploads/attachment/file/264246/Las_HSE_en_en_nuevo_modelo_educativo.pdf
- Aflatoun: https://aflatoun.org/why-social-and-financial-education/our-resources · https://aflatoun.mn.co · https://globaled.gse.harvard.edu/aflatoun-international
- Character Lab (Bridgespan): https://www.bridgespan.org/insights/developing-many-more-effective-learners/profile-character-lab-sel
