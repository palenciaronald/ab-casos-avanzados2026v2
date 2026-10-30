# Clase 2 · Viernes 30 de octubre — Pitches, entorno de trabajo, EDA y preprocesamiento

**Duración:** 4 horas · **Hito del día:** **H1** (ficha aprobada, proyecto montado, caso de negocio, EDA y preprocesamiento reproducible).

## Objetivos

Al terminar la clase 2, cada grupo tiene:

1. Una **ficha de caso aprobada** por el instructor, después de presentar su proyecto en 3 minutos.
2. El **proyecto montado y verificado**: repositorio propio creado desde la rama `feature/estudiantes`, entorno con
   Python 3.12, datos en `data/raw/`, `.env` con la conexión a Databricks (o el respaldo local),
   `especificacion-proyecto.md` completada y `CLAUDE.md` ajustado, todo subido a GitHub.
3. El **entorno de IA listo**: constitución ajustada, Spec Kit (`/speckit-…`) y subagentes funcionando en Claude Code.
4. El **caso de negocio escrito en el notebook** `01_caso_negocio` (pregunta, costos, línea base, métrica).
5. Un **EDA** que termina en decisiones escritas (mínimo 5, cada una justificada).
6. Un **preprocesamiento reproducible**: la limpieza como código, la partición por la unidad de
   análisis correcta, datos limpios y **al menos una prueba** que verifica la partición.

## Cómo se organiza la sesión

Primero se conocen los proyectos (pitches) y se deja **un entorno de trabajo común y funcionando**. Desde ahí, la clase
tiene un ritmo fijo: **el instructor explica con el ejemplo ya ejecutado (CreditSight) y, justo después, cada grupo hace lo
mismo con su proyecto**. No se programa en vivo: se recorren las decisiones de un ejemplo terminado.

| Demo | Máximo | Material |
|---|---|---|
| **Entorno** (dentro del bloque de entorno) | 10 min | `diapositivas/00-montaje-del-proyecto.md` |
| **A · Caso de negocio** | 10 min | notebook `01_caso_negocio` (`diapositivas/01-caso-eda-preproc.md`, secciones 1–3, diap. 3–5) |
| **B · EDA** | 20 min | `diapositivas/01-caso-eda-preproc.md` (secciones 4–8, diap. 6–10) · notebook `02_eda` |
| **C · Preprocesamiento y fuga** | 20 min | `diapositivas/01-caso-eda-preproc.md` (secciones 9–13, diap. 11–15) · notebook `03_preprocesamiento` |

Los notebooks de la clase (los del instructor y los esqueletos de los estudiantes) están en `notebooks/`.

## Agenda

| Hora | Min | Bloque | Material |
|---|---|---|---|
| 0:00–0:30 | 30 | **Pitches:** 10 grupos × **3 min máximo** (el instructor aprueba o devuelve las fichas) | `curso/evaluacion/revision-de-fichas.md` |
| 0:30–1:10 | 40 | **Entorno de trabajo:** repo, datos, `.env`, Claude Code, Spec Kit, constitución, subagentes | `curso/guias/montaje-proyecto.md`, `curso/guias/entorno-ia-specify.md` |
| 1:10–1:20 | 10 | **Demo A:** caso de negocio | `01_caso_negocio` del instructor |
| 1:20–1:35 | 15 | Trabajo de grupos: **caso de negocio** en su notebook | `notebooks/01_caso_negocio.ipynb` |
| 1:35–1:55 | 20 | **Demo B:** EDA | `diapositivas/01-caso-eda-preproc.md` (diap. 6–10) |
| 1:55–2:35 | 40 | Trabajo de grupos: **EDA** | `curso/kit-estudiante/guia-eda-y-preprocesamiento.md`, `especificaciones/02-eda.md` |
| 2:35–2:45 | 10 | Descanso | — |
| 2:45–3:05 | 20 | **Demo C:** preprocesamiento y fuga | `diapositivas/01-caso-eda-preproc.md` (diap. 11–15) |
| 3:05–3:50 | 45 | Trabajo de grupos: **limpieza, partición y pruebas** | `especificaciones/03-preprocesamiento.md`, `curso/kit-estudiante/checklist-revision-ia.md` |
| 3:50–4:00 | 10 | **Cierre de H1** (1 min por grupo) y tarea autónoma | `specs/001-curso-v2-end-to-end/contracts/etapas.md` |

La lista de control del instructor (puntos de control y banco de preguntas orales) está en
`lista-de-control.md`.

> **Los tiempos son tope, no meta.** Los pitches de 3 minutos con 10 grupos ocupan los 30 minutos **sin preguntas ni cambios de
> turno**: usa cronómetro visible, las preguntas van a los puntos de control, y los grupos pasan en orden para que el siguiente
> esté de pie cuando termina el anterior.

## Detalle por bloque

### 0:00 · Pitches (30 min)
- **10 grupos, 3 minutos cada uno, ni uno más.** Sin diapositivas: de pie o desde la mesa, con la ficha a la vista.
- **Qué debe decir cada grupo (en este orden):** (1) la pregunta de negocio en una frase, (2) el dataset (de dónde, cuántas filas),
  (3) **qué es una fila** y si hay entidades repetidas, (4) qué error cuesta más y qué métrica usarán.
- **Tú, mientras escuchas:** marca los 11 criterios de `revision-de-fichas.md` en la hoja de registro. No interrumpas; anota la
  pregunta para después.
- **Decisión:** `aprobada` o `devuelta`, con observación concreta. Se anuncia **al final de los 30 minutos**, no grupo por
  grupo. Los devueltos corrigen **durante el bloque de entorno** y te lo muestran antes de la demo A.
- **Regla:** ningún grupo avanza al EDA sin ficha aprobada. El que no la tenga a las 1:55 se sienta contigo (plan de rescate
  en `revision-de-fichas.md`).
- Las fichas se leen **la víspera**: el pitch es para presentarlas, no para descubrirlas.

### 0:30 · Entorno de trabajo (40 min)
Todo en una sola pasada, con el instructor mostrando en pantalla y los grupos haciendo lo mismo en sus equipos:

1. **Repositorio y datos (≈ 15 min):** una persona crea el repo vacío en GitHub y clona la rama `feature/estudiantes` apuntándola
   a su repo; los demás clonan **el del grupo**. Nombre del paquete, entorno de Python 3.12, `.env`, dataset en `data/raw/`,
   `python scripts/verificar_entorno.py` sin `FALTA`, primer push. Guía: `curso/guias/montaje-proyecto.md`.
2. **Claude Code funcionando (≈ 5 min):** abierto **dentro de la carpeta del repo**; comprobar que lee `CLAUDE.md`.
3. **Entorno de IA (≈ 20 min):** guía `curso/guias/entorno-ia-specify.md`. Se ajusta la **constitución** con
   `/speckit-constitution`, se comprueba que aparecen los `/speckit-…`, se conocen los **tres subagentes** (`/agents`) y se
   explica qué es una **especificación** (`especificaciones/`, `specs/`) y un **`tasks.md`** (la lista de trabajo del grupo).
   Crear un subagente propio queda de tarea antes de la clase 4.

- **Databricks hoy no bloquea:** la conexión se usa desde la clase 3 (`MLFLOW_FORCE_LOCAL=1` si no conecta). Si no alcanza el
  tiempo, el grupo la termina de tarea esta noche con `curso/guias/databricks-mlflow.md`.
- **Punto de control 1 (1:10):** ficha aprobada, repo clonado por todos con el primer push hecho, `verificar_entorno.py` sin
  `FALTA`, constitución ajustada con el nombre del proyecto y `/speckit` visible. Quien no llega pasa a apoyo individual; no
  se bloquea la clase.
- Se necesita **una persona de apoyo**: este es el bloque con más dudas técnicas.

### 1:10 · Demo A — Caso de negocio (10 min) y trabajo (15 min)
- **Demo:** `01_caso_negocio` de CreditSight: la pregunta de negocio, la **matriz de costos** (equivocarse no cuesta lo mismo),
  la línea base de dos estrategias sin modelo y la métrica de éxito. Es la ficha aprobada convertida en números.
- **Trabajo (15 min):** cada grupo completa **su** `notebooks/01_caso_negocio.ipynb` con lo que dijo en el pitch: pregunta,
  quién decide y cómo, qué cuesta cada error, línea base y métrica. Lo mismo queda resumido en `reports/00_caso.md`.
- Pregunta para los grupos: *¿cuál de sus dos errores cuesta más, y cuántas veces más?*

### 1:35 · Demo B — EDA (20 min) y trabajo (40 min)
- **Demo:** secciones 4–8 (diap. 6–10) y `02_eda`. Hilo: **cada hallazgo termina en una decisión escrita**
  (tabla de 10 decisiones de CreditSight en `ejemplo/reports/01_eda.md`). Puntos a subrayar: datos que llegan como texto →
  basura; salto brusco tras p95–p97 → corrupción; variables que **deberían** ser estables; vacío que significa algo.
- **Trabajo:** primeros 10 min, secciones 1 y 2 de `especificaciones/02-eda.md` (qué esperan y qué van a medir) **antes** de abrir
  el notebook. Después trabajan en `notebooks/02_eda.ipynb` y completan las secciones 3 y 4.
- Preguntas para los grupos: *¿qué variable de su dataset debería ser estable y no lo es? ¿qué significa un vacío?*
- **Punto de control 2 (2:20):** **al menos 3 decisiones** escritas con su motivo (las 5 se cierran en el bloque siguiente).
  Preguntar a un integrante distinto de quien escribió: *¿por qué esa decisión?*

### 2:45 · Demo C — preprocesamiento y fuga (20 min) y trabajo (45 min)
- **Demo:** secciones 9–13 (diap. 11–15) y `03_preprocesamiento`. De decisiones a **código con pruebas** (`src/<paquete>/data/`);
  el notebook solo orquesta.
- **Momento central (5 min):** la fuga por partición. Mismo modelo y datos; solo cambia cómo se parte:

  | Partición | Clientes en ambos lados | F1 macro | Costo esperado |
  |---|---|---|---|
  | Por fila (mal) | 10.449 | 0,734 | 0,65 |
  | Por cliente (bien) | 0 | 0,695 | 0,73 |

- Pregunta de transferencia: *¿cuál es su unidad de análisis? ¿qué se repite en sus filas?*
- **Trabajo:** primeros 10 min, `especificaciones/03-preprocesamiento.md` completa **antes** de pedirle código a Claude. Luego
  convierten las decisiones del EDA en código y crean al menos una prueba de la **partición por su unidad de análisis**. Revisan
  lo que genera Claude con los subagentes `revisor-de-codigo-ia`, `escritor-de-pruebas` y `auditor-de-fuga`, y con
  `kit-estudiante/checklist-revision-ia.md` (¿corre desde cero?, ¿filtra información?, ¿se entiende cada línea?).
- **Punto de control 3 (3:40):** cada grupo muestra (1) la limpieza corriendo de principio a fin, (2) cómo parte los datos y por
  qué, y (3) `pytest` en verde. Ningún grupo termina sin declarar su unidad de análisis por escrito.

### 3:50 · Cierre de H1 (10 min)
- **Un minuto por grupo:** su unidad de análisis y un hallazgo que no esperaban.
- Qué falta por grupo, según los criterios de **H1** (abajo).
- **Tarea para esta noche (la clase 3 es mañana, sábado 31 de octubre):** dejar el repositorio en orden y **subido a GitHub**
  (con lo pendiente de H1 si lo hay), terminar la conexión con Databricks si quedó pendiente, y leer
  `curso/kit-estudiante/guia-modelado-y-optimizacion.md`. **No hay que dejar el pipeline base hecho:** la clase 3 empieza
  construyéndolo (preprocesamiento + un modelo simple) antes de entrar a las variables.

## Criterios de aceptación de H1

Tomados de `specs/001-curso-v2-end-to-end/contracts/etapas.md`:

- **Ficha aprobada.**
- **Proyecto montado**: repo creado desde la rama `feature/estudiantes`, entorno verificado y primer push.
- **EDA con al menos 5 decisiones justificadas** (`reports/01_eda.md`).
- **Partición por la unidad correcta, documentada** y verificada con una prueba.
- **Limpieza reproducible por script**: corre de principio a fin desde el repositorio del grupo.

## Qué entrega cada grupo al terminar

| Entregable | Dónde |
|---|---|
| Ficha de caso aprobada | `reports/00_caso.md` |
| Proyecto montado | repo propio en GitHub, `.env` (no se sube), `especificacion-proyecto.md` completada |
| Entorno de IA | `.specify/memory/constitution.md` ajustada, subagentes probados, commit subido |
| Caso de negocio | `notebooks/01_caso_negocio.ipynb` |
| EDA con decisiones | `notebooks/02_eda.ipynb` y `reports/01_eda.md` |
| Especificaciones llenas | `especificaciones/02-eda.md` y `especificaciones/03-preprocesamiento.md` |
| Limpieza y partición como código | `src/<paquete>/data/` + `tests/` |
| Datos limpios y partición | `data/processed/` (se regeneran con el notebook 03) |
| **Sección del reporte** de caso y EDA | `reports/` (primera parte del informe técnico) |

## Reglas de la sesión

- **La prueba no se toca:** se guarda la partición y no se vuelve a mirar hasta la etapa de
  validación final.
- **Decisiones antes que código:** primero la decisión con su motivo, luego el código.
- **Especificación antes que código:** `especificaciones/` se llena antes de pedirle algo a Claude.
- **Sin ficha aprobada no hay EDA.**
- **Sin `.env` en GitHub:** si el script de verificación marca `.env` fuera de `.gitignore`, se arregla antes de cualquier push.
- **Cada integrante explica lo que generó la IA:** el instructor pregunta a quien no escribió el código.

## Lo que el instructor debe tener listo

- [ ] `00-montaje-del-proyecto.md` y `01-caso-eda-preproc.md` exportados a HTML; notebooks `01`–`03` de `ejemplo/` ejecutados y abiertos.
- [ ] Fichas de la clase 1 **leídas la víspera**, con los 11 criterios marcados y observaciones listas (`revision-de-fichas.md`).
- [ ] `lista-de-control.md` impresa o abierta, con una fila por grupo (10 grupos).
- [ ] Cronómetro visible para los pitches (3 min) y para cada bloque.
- [ ] Un repositorio de GitHub de prueba y un `.env` válido para demostrar el montaje sin imprevistos.
- [ ] La rama `feature/estudiantes` clonada en una carpeta de prueba, con Claude Code abierto **dentro**: `/speckit` y `/agents`
  visibles. Si algún grupo usa Mac, `pwsh` instalado.
- [ ] `ejemplo/reports/00_caso.md`, `ejemplo/reports/01_eda.md` y `ejemplo/especificacion-proyecto.md` a mano como modelos.
- [ ] Una persona de apoyo para el bloque de entorno (es el de más dudas técnicas).
