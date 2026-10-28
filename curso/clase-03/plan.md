# Clase 3 · Sábado 31 de octubre (semana 1) — Pipeline base, variables, torneo y optimización con tracking

**Duración:** 4 horas · **Hito del día:** avance de **H2** (el hito se cierra el **jueves 5 de noviembre**, en la clase 4): pipeline base,
variables medidas, torneo con la misma validación y optimización con seguimiento (tracking).

> **Contexto del calendario.** Entre la clase 2 (viernes 30) y esta solo hay **una noche**, así que hoy se **construye** el
> pipeline base en la apertura. Después de esta clase vienen **5 días de trabajo autónomo** antes de la clase 4.

## Objetivos

Al terminar hoy, cada grupo tiene:

1. **Un pipeline base que corre** (preprocesamiento de H1 + un modelo simple), **construido y comprobado en la apertura**.
2. **Variables tratadas como hipótesis**: al menos 2 ideas **medidas** contra el ruido de la validación, cada una
   con su decisión (conservar o descartar) y su motivo.
3. **Un torneo de modelos** con la **misma validación por la unidad de análisis**, una tabla comparativa con
   dispersión y baseline, y **finalistas elegidos con motivo**.
4. **Una optimización con seguimiento**: al menos 1 ejecución por candidato registrada (MLflow local, sin
   Databricks) y la **mejora comprobada en datos reservados** que la búsqueda no vio.
5. Las secciones del reporte de variables, torneo y optimización.

## Cómo se organiza la sesión

La clase alterna **tres demos cortas** con **tres bloques de trabajo de grupos**. Cada demo ocurre justo antes de que
los grupos hagan esa etapa. Las demos 1 y 2 salen del mismo deck; la demo 3 tendrá el suyo.

| Demo | Máximo | Material |
|---|---|---|
| **1 · Variables como hipótesis** | 20 min | `diapositivas/02-features-torneo.md`, **diap. 1–8** · notebook `04_features` |
| **2 · Torneo de modelos** | 20 min | `diapositivas/02-features-torneo.md`, **diap. 9–16** · notebook `05_torneo` |
| **3 · Optimización con tracking** | 20 min | `diapositivas/03-optimizacion-tracking.md` (**en preparación**: depende de los resultados de la etapa 6) · notebook `06_optimizacion` |

> Las notas del presentador del deck proponen una sola charla de 20 minutos (variables, costo y torneo). Este plan la
> **parte en dos demos** para que cada una quede pegada a su bloque de trabajo; la distribución de tiempos de las
> notas del deck **no aplica**: manda este plan.

**No se programa en vivo:** se recorren las decisiones de notebooks ya ejecutados (`ejemplo/notebooks/04_features`,
`05_torneo` y, cuando exista, `06_optimizacion`). El kit de los grupos trae `curso/kit-estudiante/guia-modelado-y-optimizacion.md`
(en preparación) y los prompts de las etapas 4–6 de `curso/kit-estudiante/prompts-por-etapa.md`.

> **Estado de los materiales de hoy:** demos 1 y 2 y notebooks `04` y `05` del ejemplo, listos. **En preparación:**
> demo 3, notebook `06_optimizacion` ejecutado (la etapa 6 aún no se corrió), esqueletos de notebook de los grupos para
> las etapas 4–6 y el módulo de tracking de la plantilla (`src/proyecto/tracking/mlflow_utils.py`).

## Agenda

| Hora | Min | Bloque | Material |
|---|---|---|---|
| 0:00–0:30 | 30 | **Apertura:** estado de H1 y **construcción del pipeline base** | `lista-de-control.md`, `curso/kit-estudiante/prompts-por-etapa.md` (secciones 3 y 5) |
| 0:30–0:50 | 20 | **Demo 1:** variables como hipótesis | `diapositivas/02-features-torneo.md` (diap. 1–8) |
| 0:50–1:30 | 40 | Trabajo de grupos: **variables** | `curso/kit-estudiante/guia-modelado-y-optimizacion.md` |
| 1:30–1:40 | 10 | Descanso | — |
| 1:40–2:00 | 20 | **Demo 2:** torneo de modelos | `diapositivas/02-features-torneo.md` (diap. 9–16) |
| 2:00–2:50 | 50 | Trabajo de grupos: **torneo** | `curso/kit-estudiante/prompts-por-etapa.md` (sección 5) |
| 2:50–3:10 | 20 | **Demo 3:** optimización con tracking | `diapositivas/03-optimizacion-tracking.md` (en preparación) |
| 3:10–3:45 | 35 | Trabajo de grupos: **optimización y seguimiento** | `curso/guias/databricks-mlflow.md` |
| 3:45–4:00 | 15 | **Cierre** y tarea de 5 días de trabajo autónomo | `specs/001-curso-v2-end-to-end/contracts/etapas.md` |

La lista de control del instructor (puntos de control y banco de preguntas orales) está en `lista-de-control.md`.

## Detalle por bloque

### 0:00 · Apertura: estado de H1 y pipeline base (30 min)
- **Primeros 10 minutos:** pasar por cada grupo y **comprobar con tus ojos** el estado de H1 (cerrado ayer, viernes 30): ficha
  aprobada, EDA con decisiones, limpieza y partición como código y `pytest` en verde. Lo que quedó pendiente de la clase 2
  se anota; no se resuelve aquí.
- **Siguientes 20 minutos: construir el pipeline base desde cero.** Como entre la clase 2 y esta solo hay una noche, el
  pipeline base **no viene de tarea**: cada grupo ejecuta de principio a fin el preprocesamiento de H1 y entrena **un modelo
  simple** (el baseline) con validación por su unidad de análisis, usando los prompts de las secciones 3 y 5 del kit. Si
  falla, ese grupo se sienta contigo: sin pipeline base no hay variables ni torneo.
- Cada grupo confirma cuál es su **unidad de análisis** (la validación de hoy va por ella) y su **métrica de negocio**.
- Hoy **no se necesita Databricks**: el seguimiento es **MLflow local**. Si algún grupo ya conectó, puede registrar allí, pero no se exige; nadie se bloquea por la conexión.

### 0:30 · Demo 1 — variables como hipótesis (20 min)
- Diapositivas 1–8 de `02-features-torneo.md` y notebook `04_features`. Hilo: **cada variable nueva es una hipótesis**
  que se mide contra el ruido de la validación, no se añade porque "suena bien".
- Cifras que se muestran (de `ejemplo/reports/04_features_tabla.csv`, 5 pliegues por cliente, LightGBM fijo):

  | Variante | Costo | ± pliegues | Mejora / ruido |
  |---|---|---|---|
  | base, sin `Credit_Mix` | 0,4955 | 0,0086 | −0,70 |
  | **base, con `Credit_Mix` (referencia)** | **0,4894** | 0,0075 | 0,00 |
  | + razones financieras | 0,4896 | 0,0069 | −0,02 |
  | + historial del mes anterior | 0,4842 | 0,0081 | 0,64 |
  | + razones + historial | 0,4834 | 0,0088 | 0,69 |

- **Momentos a subrayar:** (1) *ver diferencia ≠ mejorar el modelo*: la mediana de `debt_to_income` separa las clases
  (Poor 0,063 · Standard 0,022 · Good 0,012) y aun así la variable no aporta; (2) **resultado negativo honesto**: dos
  de tres ideas razonables no sirvieron; (3) `Credit_Mix` aporta sobre todo a la calidad de las probabilidades (log
  loss de 0,6953 a 0,6686), **con una condición de negocio** (que se conozca al decidir).
- **Preguntas para los grupos:** *¿qué idea de variable van a medir antes de incluirla? ¿qué esperan que pase?*

### 0:50 · Trabajo de grupos — variables (40 min)
- Cada grupo trabaja en el notebook de variables de su repo, con la guía y el prompt de la sección 4 del kit.
- Tarea concreta: formular **al menos 2 hipótesis** de variable, medir **cada una** con la validación cruzada por su
  unidad de análisis (mismo modelo y parámetros fijos) y calcular **mejora / ruido**. La decisión (conservar o
  descartar) y su motivo se escriben en `reports/`.
- **Punto de control 1 (1:20):** el pipeline base corre **y** hay ≥ 2 hipótesis medidas con su ruido de validación (con solo
  40 minutos, basta con dos hipótesis bien medidas).
  Preguntar a un integrante distinto de quien escribió: *¿cómo saben que esa mejora no es ruido?*
- Un grupo que no llega pasa a apoyo individual durante el descanso; no se bloquea la clase.

### 1:40 · Demo 2 — torneo de modelos (20 min)
- Diapositivas 9–16 de `02-features-torneo.md` y notebook `05_torneo`. Hilo: **mismos datos, misma validación para todos**,
  un punto de referencia (baseline) y mirar la **variabilidad**, no solo el promedio.
- **Regla de decisión de menor costo esperado** (diap. 9): con LightGBM, el costo baja de 0,7722 (clase más probable)
  a 0,4894 (menor costo esperado).
- Cifras que se muestran (de `ejemplo/reports/05_torneo_tabla.csv`):

  | Modelo | Costo | ± | Recall `Poor` | s por ajuste |
  |---|---|---|---|---|
  | **random forest** | **0,4820** | 0,0077 | 0,8237 | 12 |
  | lightgbm | 0,4894 | 0,0075 | 0,8075 | 6 |
  | xgboost | 0,4900 | 0,0080 | 0,8072 | 11 |
  | regresión logística | 0,5528 | 0,0139 | 0,7743 | 4 |
  | baseline (clase más frecuente) | 1,0494 | 0,0003 | 0,0000 | 1 |

- **Métricas técnicas** (diap. 11–12, notebook `05_torneo`, sección "Las métricas técnicas"): además del costo se muestran AUC macro, PR-AUC
  de `Poor`, exactitud balanceada y recall por clase. Los tres árboles tienen un AUC casi idéntico (0,853 · 0,852 · 0,852) y la regresión
  logística queda atrás (0,819); el baseline marca el piso (0,500 de AUC, 0,291 de PR-AUC de `Poor`). **Hallazgo clave:** el recall de `Good`
  es de 0,024 a 0,142 (random forest, 0,058): la regla de menor costo casi nunca aprueba a un `Good`. *Ordenar bien no es decidir bien.*
  Estas dos diapositivas suman unos 4 minutos: abrevia la diapositiva del dinero (diap. 14) si el reloj aprieta.
- **Comparación pareada** (diap. 13): random forest gana a LightGBM y a XGBoost en **5 de 5 pliegues** (diferencia / ruido
  de 1,44 y 2,24); LightGBM y XGBoost **empatan** (0,17, gana en 2 de 5).
- **Dinero y métrica** (diap. 14–15): con 100.000 decisiones al mes, la regresión logística cuesta 7.089 unidades más que
  el mejor (el **precio** de explicarla mejor); random forest gana siendo el más conservador (recall de `Poor` 0,8237,
  F1 macro 0,5002), lo que implica más casos para el analista.
- **Decisión** (diap. 16): finalistas random forest y LightGBM. *El torneo elige finalistas, no un campeón.*
- **Preguntas para los grupos:** *¿cuál es su baseline? ¿cuál es su métrica de negocio y por qué? ¿qué modelo desempataría
  y con qué criterio que no sea la prueba?*

### 2:00 · Trabajo de grupos — torneo (50 min)
- Cada grupo compara **al menos 3 modelos más el baseline**, todos con **la misma validación por su unidad de
  análisis** (mismos pliegues), y registra media **y** desviación entre pliegues de su métrica de negocio.
- Se pide a Claude con el kit (sección 5 de los prompts) y se **revisa** con `kit-estudiante/checklist-revision-ia.md`
  (¿misma validación para todos?, ¿filtra información?, ¿se entiende cada línea?).
- **Punto de control 2 (2:40):** tabla comparativa con **dispersión y baseline**, ≥ 3 modelos con la misma validación y
  **finalistas elegidos con un motivo escrito** (consistencia pareada, tiempo, interpretabilidad o costo operativo; nunca
  la prueba). Preguntar: *¿por qué eligieron esos finalistas y no el que tuvo el número más bajo?*

### 2:50 · Demo 3 — optimización con tracking (20 min) — **en preparación**
- Deck `diapositivas/03-optimizacion-tracking.md` y notebook `06_optimizacion` del ejemplo: **aún no existen resultados**
  (la etapa 6 no se ha ejecutado). Este bloque se completa con cifras reales cuando se corra. Lo que la demo cubrirá:
  1. El **problema del tracking**: *¿cuál de las 30 pruebas de ayer era la buena?*; qué se registra (parámetros, métricas,
     etiquetas) y para qué (comparar, reproducir, auditar).
  2. **Optimizar solo los finalistas**, con un **espacio de búsqueda que lleva conocimiento** del modelo y un
     **presupuesto de ensayos acotado** (cómputo y tiempo de clase).
  3. Cada ensayo queda como ejecución **en MLflow local** (sin Databricks) y se muestra con `mlflow ui --backend-store-uri sqlite:///mlflow_local.db`. Databricks entra en la clase 4.
  4. **La mejor puntuación de la búsqueda es optimista**: se comprueba en **datos reservados** (entidades que la búsqueda nunca
     vio), con un intervalo del 95 % de la diferencia remuestreando **entidades** completas.
  5. Si la mejora **no se distingue del ruido**, se queda la configuración de partida y se reporta honestamente.
- Hasta que el deck exista, el instructor puede usar la sección de tracking de `curso/clase-01/diapositivas/nivelacion.md`
  y la guía `curso/guias/databricks-mlflow.md`.
- **Preguntas para los grupos:** *¿cuántos ensayos pueden gastar y por qué? ¿con qué datos comprobarán que la mejora es real?*

### 3:10 · Trabajo de grupos — optimización y seguimiento (35 min)
- Cada grupo optimiza **1–2 finalistas** con un **espacio de búsqueda justificado** y un presupuesto acotado, y **registra
  cada ensayo** con el módulo de tracking de su plantilla, con **MLflow local** (`configure_mlflow(force_local=True)`), siguiendo la sección de tracking de `curso/guias/databricks-mlflow.md`.
- Reservan una parte de sus **entidades** (no filas) para comprobar la mejora; comparan parámetros de partida y optimizados en
  esos datos reservados.
- **Punto de control 3 (3:40):** **al menos 1 ejecución por candidato registrada** (MLflow local; el instructor
  la ve en pantalla con `mlflow ui`) **y** la comprobación de la mejora en datos reservados, con su resultado (mejora real, no
  distinguible o empeora). Preguntar: *¿por qué su mejor puntuación de la búsqueda es optimista?*
- Un grupo sin tiempo de terminar la búsqueda deja registrado lo que tenga y completa en el trabajo autónomo; lo no negociable
  es que **haya registro** y que se **explique** cómo se comprobará la mejora.

### 3:45 · Cierre y tarea de 5 días (15 min)
- **Un minuto por grupo:** su baseline, su finalista y si la optimización mejoró de forma distinguible. El tiempo se ajusta a la
  cantidad de grupos del día.
- Revisión de lo que **falta de H2** (ver abajo): validación y prueba abierta una sola vez, registro del modelo, módulos con
  pruebas y esqueleto de la app, todo en la clase 4 (**jueves 5 de noviembre**).
- **Trabajo autónomo de 5 días (hasta el jueves 5 de noviembre):** terminar el torneo y la optimización (la búsqueda registrada
  y la mejora comprobada en datos reservados), **dejar el modelo final decidido por escrito** (modelo, parámetros y si se calibra, con
  su motivo) y escribir las secciones del reporte (`reports/04_features.md`, `reports/05_torneo.md`, `reports/06_optimizacion.md`).
  La clase 4 **empieza congelando esas decisiones antes de abrir la prueba**: quien llegue sin ellas pierde tiempo de clase.

## Criterios de aceptación de hoy (parte de H2)

Tomados de `specs/001-curso-v2-end-to-end/contracts/etapas.md`; hoy se cubren **estos dos**, y el resto de H2 se cierra el jueves 5 de noviembre (clase 4):

- **≥ 3 modelos comparados con la misma validación** (por la unidad de análisis), con tabla de dispersión y baseline.
- **≥ 1 experimento por candidato registrado** (MLflow local).

Quedan para la clase 4 (jueves 5 de noviembre): modelo final registrado con versión, `src/` con pruebas y app local que carga el modelo.

## Qué entrega cada grupo al terminar

| Entregable | Dónde |
|---|---|
| Variables medidas, con decisión y motivo | notebook de variables y `reports/04_features.md` |
| Tabla comparativa del torneo (media, dispersión y baseline) | notebook de torneo y `reports/05_torneo.md` |
| Finalistas elegidos con motivo | `reports/05_torneo.md` |
| Ejecuciones registradas de la optimización | MLflow local (`mlflow_local.db`) |
| Comprobación de la mejora en datos reservados | `reports/06_optimizacion.md` |
| **Sección del reporte** de variables, torneo y optimización | `reports/` (segunda parte del informe técnico) |

## Reglas de la sesión

- **La prueba no se toca:** todo se decide con validación; el conjunto de prueba sigue cerrado hasta la clase 4.
- **La misma validación para todos los modelos y variantes**, por la unidad de análisis (nunca por fila).
- **Una variable entra solo si mejora más que el ruido.** Ver diferencia en un gráfico no basta.
- **Sin registro no hay optimización:** cada ensayo debe quedar en MLflow (local en esta clase).
- **Cada integrante explica lo que generó la IA:** el instructor pregunta a quien no escribió el código.

## Plan B

> **Nota:** hoy no se necesita Databricks (el seguimiento es local). Las dos primeras filas quedan como nota por si algún grupo ya conectó; **no se exige** y su problema de conexión se resuelve para la clase 4.

| Situación | Qué hacer |
|---|---|
| Un grupo ya conectó con Databricks | Puede registrar allí; no se exige. Si falla, `MLFLOW_FORCE_LOCAL=1` y se sigue: hoy no se necesita Databricks |
| Cuota de Databricks agotada | No aplica hoy (el seguimiento es local); se vuelve a revisar en la clase 4 |
| Cómo ver el MLflow local | `mlflow ui --backend-store-uri sqlite:///mlflow_local.db` desde la raíz del repo (ver `curso/guias/databricks-mlflow.md`) |
| La búsqueda tarda demasiado | Reducir el presupuesto (por ejemplo, 8–12 ensayos por finalista), optimizar **solo un** finalista o usar una validación de 3 pliegues; registrar lo que haya |
| Un grupo no termina el pipeline base en la apertura | Se sienta contigo; si no se arregla en 20 minutos más, trabaja con su baseline más simple para no perder el torneo |

## Lo que el instructor debe tener listo

- [ ] `02-features-torneo.md` exportado a HTML (diap. 1–8 y 9–16 ubicadas) y notebooks `04_features` y `05_torneo` de `ejemplo/` ejecutados y abiertos.
- [ ] **Demo 3** (`03-optimizacion-tracking.md`) y notebook `06_optimizacion` **ejecutado** (en preparación; dependen de la etapa 6).
- [ ] MLflow local funcionando para la demo: abre la interfaz con `mlflow ui --backend-store-uri sqlite:///mlflow_local.db` (desde la raíz del repo; si lo corres sobre el ejemplo, la base está en `ejemplo/mlflow_local.db`) y verifica que muestra los ensayos.
- [ ] `lista-de-control.md` impresa o abierta, con una fila por grupo y los tres puntos de control.
- [ ] Estado de H1 de cada grupo revisado la noche anterior (repos y reportes de la clase 2).
- [ ] Una persona de apoyo para los bloques de torneo y de optimización (es donde más aparecen errores de validación y de conexión).
