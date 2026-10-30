# Clase 2 · Viernes 30 de octubre — Montaje, EDA y preprocesamiento

**Duración:** 4 horas · **Hito del día:** **H1** (ficha aprobada, proyecto montado, EDA y preprocesamiento reproducible).

## Objetivos

Al terminar la clase 2, cada grupo tiene:

1. Una **ficha de caso aprobada** por el instructor.
2. El **proyecto montado y verificado**: repositorio propio creado desde la rama `feature/estudiantes`, entorno con
   Python 3.12, `.env` con la conexión a Databricks (o el respaldo local), `especificacion-proyecto.md`
   completada y `CLAUDE.md` ajustado, todo subido a GitHub.
3. Un **EDA** que termina en decisiones escritas (mínimo 5, cada una justificada).
4. Un **preprocesamiento reproducible**: la limpieza como código, la partición por la unidad de
   análisis correcta, datos limpios y **al menos una prueba** que verifica la partición.
5. La **sección del reporte** de caso y EDA.

## Cómo se organiza la sesión

El caso de negocio ya se trabajó en la clase 1 (jueves 29 de octubre): hoy se **aprueba** y se pasa a montar y a analizar. El
instructor muestra el ejemplo (CreditSight) **en tres demos cortas**, cada una justo antes de que
los grupos trabajen esa etapa:

| Demo | Máximo | Material |
|---|---|---|
| **Montaje** | 10 min | `diapositivas/00-montaje-del-proyecto.md` |
| **B · EDA** | 20 min | `diapositivas/01-caso-eda-preproc.md` (secciones 4–8, diap. 6–10) · notebook `02_eda` |
| **C · Preprocesamiento y fuga** | 20 min | `diapositivas/01-caso-eda-preproc.md` (secciones 9–13, diap. 11–15) · notebook `03_preprocesamiento` |

**No se programa en vivo:** se recorren las decisiones de un ejemplo ya ejecutado. Los notebooks de
la clase (los del instructor y los esqueletos de los estudiantes) están en `notebooks/`. Las secciones 1–3
de la demo 01 (el caso de negocio) quedan como apoyo para quien necesite repasar la matriz de costos.

> Si el grupo va muy adelantado, las demos B y C se pueden dar seguidas y dedicar más tiempo al
> trabajo de grupos.

## Agenda

| Hora | Min | Bloque | Material |
|---|---|---|---|
| 0:00–0:30 | 30 | **Aprobación de fichas** (en paralelo: grupos cierran pendientes de instalación) | `curso/evaluacion/revision-de-fichas.md` |
| 0:30–1:20 | 50 | **Montaje del proyecto**: demo (10) + trabajo de grupos (40) | `curso/guias/montaje-proyecto.md`, `scripts/verificar_entorno.py` |
| 1:20–1:40 | 20 | **Entorno de desarrollo con IA:** constitución, Spec Kit y subagentes | `curso/guias/entorno-ia-specify.md` (pasos 12.1 a 12.4) |
| 1:40–2:00 | 20 | **Demo B:** EDA | `diapositivas/01-caso-eda-preproc.md` (diap. 6–10) |
| 2:00–2:40 | 40 | Trabajo de grupos: **EDA** | `curso/kit-estudiante/guia-eda-y-preprocesamiento.md` |
| 2:40–2:50 | 10 | Descanso | — |
| 2:50–3:10 | 20 | **Demo C:** preprocesamiento y fuga | `diapositivas/01-caso-eda-preproc.md` (diap. 11–15) |
| 3:10–3:50 | 40 | Trabajo de grupos: **limpieza, partición y pruebas** | `curso/kit-estudiante/checklist-revision-ia.md` |
| 3:50–4:00 | 10 | **Cierre de H1** y tarea autónoma | `specs/001-curso-v2-end-to-end/contracts/etapas.md` |

La lista de control del instructor (puntos de control y banco de preguntas orales) está en
`lista-de-control.md`.

## Detalle por bloque

### 0:00 · Aprobación de fichas (30 min)
- Devolver las fichas de la clase 1: **aprobadas**, **devueltas** (con observaciones concretas) o
  **pendientes**. El protocolo y las observaciones modelo están en `curso/evaluacion/revision-de-fichas.md`.
- Mientras el instructor pasa por cada grupo, **los demás** terminan lo que quedó pendiente de la
  instalación de la clase 1 (`python scripts/verificar_entorno.py`) y empiezan el montaje (una persona crea el repo vacío y clona la rama `feature/estudiantes`; los demás clonan el repo del grupo).
- **Regla:** ningún grupo avanza al EDA sin ficha aprobada. Un grupo sin caso a las 0:30 se sienta con
  el instructor durante el montaje (plan de rescate en `revision-de-fichas.md`).

### 0:30 · Montaje del proyecto (50 min)
- **Demo (10 min):** `00-montaje-del-proyecto.md`. Se muestra cómo está montado `ejemplo/`: mapa del
  repo, `.env` y Databricks (perfil o token, `EXPERIMENT_DIR`, respaldo local), `especificacion-proyecto.md`,
  `CLAUDE.md` y el script de verificación.
- **Trabajo de grupos (40 min):** cada grupo sigue `curso/guias/montaje-proyecto.md`: repo propio (clonado
  de la rama `feature/estudiantes`), entorno, `.env`, carpeta de experimentos en Databricks, especificación completada con su
  ficha, dataset en `data/raw/`, primer commit y push.
- **Punto de control 1 (1:20):** ficha aprobada **y** `python scripts/verificar_entorno.py` sin ningún
  `FALTA` **y** primer push hecho. Un grupo que no llega pasa a apoyo individual; no se bloquea la clase.
- En la demo del montaje, **3 min** para mostrar el entorno de IA (constitución, `/speckit`, `/agents`): `00-montaje-del-proyecto.md`, diap. 7.
- Si Databricks no conecta, se pone `MLFLOW_FORCE_LOCAL=1` y se sigue: el aviso del script lo indica.

### 1:40 · Demo B — EDA (20 min)
- Secciones 4–8 de la demo (diap. 6–10) y `02_eda`. Hilo: **cada hallazgo termina en una decisión escrita**
  (tabla de 10 decisiones de CreditSight en `ejemplo/reports/01_eda.md`).
- Puntos a subrayar: datos que llegan como texto → basura; salto brusco tras p95–p97 → corrupción;
  variables que **deberían** ser estables; vacío que significa algo ("sin préstamos").
- Preguntas para los grupos: *¿qué variable de su dataset debería ser estable y no lo es? ¿qué
  significa un vacío en su dataset?*

### 1:20 · Entorno de desarrollo con IA (20 min)
- Con el repo ya subido, cada grupo sigue `curso/guias/entorno-ia-specify.md`: **12.1** ajustar la constitución con
  `/speckit-constitution` (10 min, una sola pantalla), **12.2** comprobar `/speckit-…` (y `pwsh` en Mac), **12.3** conocer los
  tres subagentes (`/agents`) y **12.4** crear uno propio si da el tiempo (si no, queda de tarea antes de la clase 4).
- **Todo viene instalado** en la rama `feature/estudiantes` (`.specify/`, `.claude/skills/`, `.claude/agents/`) y viaja con el repo.
- **Punto de control 1b (1:40):** constitución con el nombre del proyecto y la unidad de análisis, `/speckit-…` y `/agents`
  visibles, y un commit subido. Preguntar a quien no escribió la constitución: *¿qué principio es el más importante y por qué?*
- Hoy **no** se recorre el flujo completo (specify → plan → tasks → implement): se practica con la limpieza si sobra tiempo
  y es obligatorio desde la clase 3. El `tasks.md` es la lista de trabajo del grupo.

### 2:00 · Trabajo de grupos — EDA (40 min)
- Primeros 10 min: cada grupo llena las secciones 1 y 2 de `especificaciones/02-eda.md` (qué esperan encontrar y qué van a medir) **antes** de abrir el notebook.
- Cada grupo trabaja en `notebooks/02_eda.ipynb` de su repo (esqueleto de la plantilla), con la guía
  `guia-eda-y-preprocesamiento.md` y el kit de prompts por etapa; completa las secciones 3 y 4 de la especificación.
- **Punto de control 2 (2:30):** cada grupo tiene una lista de **al menos 3 decisiones** ya escritas con
  su motivo (las 5 completas se cierran en el bloque siguiente). Preguntar a un integrante distinto de
  quien escribió: *¿por qué esa decisión?*

### 2:50 · Demo C — preprocesamiento y fuga (20 min)
- Secciones 9–13 de la demo (diap. 11–15) y `03_preprocesamiento`. Hilo: de decisiones a **código con pruebas**
  (`src/<paquete>/data/`); el notebook solo orquesta.
- **Momento central (5 min):** la fuga por partición. Mismo modelo y datos; solo cambia cómo se parte:

  | Partición | Clientes en ambos lados | F1 macro | Costo esperado |
  |---|---|---|---|
  | Por fila (mal) | 10.449 | 0,734 | 0,65 |
  | Por cliente (bien) | 0 | 0,695 | 0,73 |

- Pregunta de transferencia: *¿cuál es su unidad de análisis? ¿qué se repite en sus filas?*

### 3:10 · Trabajo de grupos — limpieza, partición y pruebas (40 min)
- Primeros 10 min: cada grupo llena `especificaciones/03-preprocesamiento.md` (unidad, partición, reglas, pruebas) **antes** de pedirle código a Claude.
- Cada grupo convierte sus decisiones del EDA en código en `src/<paquete>/data/` y crea al menos una
  prueba que verifica la **partición por su unidad de análisis**.
- Se pide a Claude con el kit, pero con la regla del curso: **revisar el resultado** con los subagentes `revisor-de-codigo-ia` y `auditor-de-fuga` y con
  `kit-estudiante/checklist-revision-ia.md` (¿corre desde cero?, ¿filtra información?, ¿se entiende
  cada línea?).
- **Punto de control 3 (3:40):** cada grupo muestra (1) la limpieza corriendo de principio a fin,
  (2) cómo parte los datos y por qué, y (3) `pytest` en verde. Ningún grupo termina sin declarar su
  unidad de análisis por escrito.

### 3:50 · Cierre de H1 (10 min)
- **Un minuto por grupo:** su unidad de análisis y un hallazgo que no esperaban. El tiempo se ajusta
  a la cantidad de grupos del día.
- Revisión de los criterios de **H1** (abajo) y qué falta por grupo.
- **Tarea para esta noche (la clase 3 es mañana, sábado 31 de octubre):** dejar el repositorio en orden y **subido a GitHub**
  (con lo pendiente de H1 si lo hay), y leer `curso/kit-estudiante/guia-modelado-y-optimizacion.md`. **No hay que dejar
  el pipeline base hecho:** la clase 3 empieza construyéndolo (preprocesamiento + un modelo simple) antes de entrar a las variables.

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
| EDA con decisiones | `notebooks/02_eda.ipynb` y `reports/01_eda.md` |
| Limpieza y partición como código | `src/<paquete>/data/` + `tests/` |
| Entorno de IA | `.specify/memory/constitution.md` ajustada, subagentes probados, commit subido |
| Especificaciones llenas | `especificaciones/02-eda.md` y `especificaciones/03-preprocesamiento.md` |
| Datos limpios y partición | `data/processed/` (se regeneran con el notebook 03) |
| **Sección del reporte** de caso y EDA | `reports/` (primera parte del informe técnico) |

## Reglas de la sesión

- **La prueba no se toca:** se guarda la partición y no se vuelve a mirar hasta la etapa de
  validación final.
- **Decisiones antes que código:** primero la decisión con su motivo, luego el código.
- **Sin ficha aprobada no hay EDA.**
- **Sin `.env` en GitHub:** si el script de verificación marca `.env` fuera de `.gitignore`, se arregla antes de cualquier push.
- **Cada integrante explica lo que generó la IA:** el instructor pregunta a quien no escribió el código.

## Lo que el instructor debe tener listo

- [ ] `00-montaje-del-proyecto.md` y `01-caso-eda-preproc.md` exportados a HTML; notebooks `01`–`03` de `ejemplo/` ejecutados y abiertos.
- [ ] Fichas de la clase 1 revisadas con observaciones concretas (`revision-de-fichas.md`).
- [ ] `lista-de-control.md` impresa o abierta, con una fila por grupo.
- [ ] Un repositorio de GitHub de prueba y un `.env` válido para demostrar el montaje sin imprevistos.
- [ ] La rama `feature/estudiantes` clonada en la carpeta de prueba, con Claude Code abierto **dentro**: `/speckit` y `/agents` visibles. Si algún grupo usa Mac, `pwsh` instalado.
- [ ] `ejemplo/reports/00_caso.md`, `ejemplo/reports/01_eda.md` y `ejemplo/especificacion-proyecto.md` a mano como modelos.
- [ ] Una persona de apoyo para el bloque de montaje (es el de más dudas técnicas).
