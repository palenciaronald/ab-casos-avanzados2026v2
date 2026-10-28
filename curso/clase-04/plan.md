# Clase 4 · Jueves 5 de noviembre (semana 2) — Validación, registro del modelo y app local

**Duración:** 4 horas · **Hito del día:** **H2** (modelos comparados y registrados, prueba abierta una sola vez, modelo final
registrado con versión, `src/` con pruebas y app local que carga el modelo).

> **Calendario del curso.** Seis clases de 4 horas en dos semanas de tres días seguidos: clase 1 (jue 29 oct), clase 2
> (vie 30 oct), clase 3 (sáb 31 oct) · **cinco días de trabajo autónomo** · clase 4 (jue 5 nov, hoy), clase 5 (vie 6 nov) y
> clase 6 (sáb 7 nov). H1 se cerró el viernes 30 de octubre; hoy se cierra **H2**; H3 es mañana (clase 5) y H4, el
> domingo 15 de noviembre.

## Objetivos

Al terminar la clase, cada grupo tiene:

1. **Decisiones congeladas por escrito antes de tocar la prueba** (modelo, parámetros, ¿calibrar?, métrica, regla de decisión).
2. **La prueba abierta una sola vez**, con **intervalo remuestreando entidades**, **comparación con el baseline**,
   **errores por segmento** (o carga de trabajo) y una **interpretación** con sus límites.
3. **El modelo final registrado con versión y alias** (Databricks o MLflow local) y **exportado** a `models/model.joblib`
   desde el registro, junto con `models/input_schema.json` y la **ficha del modelo** iniciada.
4. **`src/` con pruebas**: la inferencia rechaza datos imposibles y el esquema se guarda y se recarga; `pytest` en verde.
5. **Una app que corre en local** (`streamlit run app/streamlit_app.py`) y carga ese modelo.
6. Las secciones del reporte de validación y de registro.

## Cómo se organiza la sesión

Los grupos llegan después de **cinco días de trabajo autónomo** con la clase 3 terminada: variables medidas, torneo con
finalistas, optimización registrada y un **modelo final tentativo** con motivo. La clase alterna **tres demos cortas** con
**tres bloques de trabajo de grupos**.

| Demo | Máximo | Material |
|---|---|---|
| **1 · Validación e interpretación** | 20 min | `diapositivas/04-validacion-interpretacion.md` (**en preparación**) · notebook `07_validacion_interpretacion` del ejemplo (**por generar y ejecutar**: aún no existe el archivo) |
| **2 · Registro del modelo e inferencia** | 20 min | `diapositivas/05-registro-inferencia-app.md`, parte de registro e inferencia (**en preparación**) · notebooks `08_registro_modelo` y `09_inferencia` del ejemplo (**por generar y ejecutar**: aún no existen los archivos) |
| **3 · De notebook a módulos con pruebas, y esqueleto de la app** | 20 min | `diapositivas/05-registro-inferencia-app.md`, parte de módulos y app (**en preparación**) · `ejemplo/src/creditsight/inference/` y `ejemplo/app/streamlit_app.py` |

> **Estado de los materiales de hoy.** Los notebooks `07`, `08` y `09` del ejemplo **todavía no existen como archivos** en
> `ejemplo/notebooks/` (hay que generarlos y ejecutarlos) y las diapositivas de las demos **dependen de la etapa de
> optimización (etapa 6), que tampoco se ha ejecutado**: sin ella no existen el modelo final, el `model.joblib` ni el
> esquema del ejemplo. **No cites cifras de CreditSight para esta clase hasta que existan.** Lo que
> ya está listo: este plan, la lista de control, la guía `curso/kit-estudiante/guia-validacion-registro-y-app.md`, los
> esqueletos de notebook de los grupos (`07`, `08`, `09`), la plantilla de la app y los módulos de inferencia con sus
> pruebas.

**No se programa en vivo:** se recorren las decisiones de notebooks ya ejecutados (cuando existan). La app de los grupos sale
de la **plantilla** (`app/streamlit_app.py`, genérica: arma su formulario desde `models/input_schema.json`), así que
**nadie tiene que construirla desde cero**.

## Agenda

| Hora | Min | Bloque | Material |
|---|---|---|---|
| 0:00–0:20 | 20 | **Apertura:** estado del trabajo autónomo y **decisiones congeladas por escrito** | `lista-de-control.md` |
| 0:20–0:40 | 20 | **Demo 1:** validación e interpretación | `diapositivas/04-validacion-interpretacion.md` (en preparación) |
| 0:40–1:35 | 55 | Trabajo de grupos: **validación e interpretación** | `curso/kit-estudiante/guia-validacion-registro-y-app.md` (secciones 1–4) |
| 1:35–1:45 | 10 | Descanso | — |
| 1:45–2:05 | 20 | **Demo 2:** registro del modelo e inferencia | `diapositivas/05-registro-inferencia-app.md` (en preparación) |
| 2:05–2:50 | 45 | Trabajo de grupos: **registrar, exportar y ficha del modelo** | `curso/guias/databricks-mlflow.md`, guía (secciones 5–7) |
| 2:50–3:10 | 20 | **Demo 3:** módulos con pruebas y esqueleto de la app | `diapositivas/05-registro-inferencia-app.md` (en preparación) |
| 3:10–3:45 | 35 | Trabajo de grupos: **módulos, pruebas y app local** | guía (secciones 8–9) |
| 3:45–4:00 | 15 | **Cierre de H2** y tarea para la clase 5 | `specs/001-curso-v2-end-to-end/contracts/etapas.md` |

La lista de control del instructor (puntos de control y banco de preguntas orales) está en `lista-de-control.md`.

## Detalle por bloque

### 0:00 · Apertura (20 min)
- **Cinco días de trabajo autónomo** terminan hoy: pasa por cada grupo y anota qué trae hecho (variables, torneo, optimización
  registrada, modelo final tentativo) y qué le falta. Lo que falte se anota; no se resuelve aquí.
- **El ritual de las decisiones congeladas:** cada grupo escribe, en la sección 1 del notebook de validación y en
  `reports/07_validacion.md`, el **modelo final**, los **parámetros** (optimizados o de partida), si **calibra**, la **métrica
  principal**, la **regla de decisión** y la **fecha y hora**. **Tú lo ves escrito antes de que nadie abra la prueba.**
- Regla para elegir sin mirar la prueba: parámetros optimizados **solo si la mejora fue distinguible del ruido**; entre
  finalistas, el de menor pérdida en los datos reservados, y el más simple si empatan.
- Pregunta a quien no lo escribió: *¿qué decidieron y con qué datos?* Un grupo que **ya miró la prueba** para decidir algo lo
  declara hoy y lo deja escrito en el reporte (no se le castiga: se le pide honestidad).
- **Hoy se conectan por primera vez a Databricks** (en la clase 3 el seguimiento fue local): se usa para **registrar el modelo final** con alias `champion` en Unity Catalog. Si algún grupo no tiene `.env` o no conecta, recuérdale el **plan B** (abajo): el registro local cuenta igual para H2 y hoy no se bloquea a nadie.

### 0:20 · Demo 1 — validación e interpretación (20 min)
- Diapositivas `04-validacion-interpretacion.md` y notebook `07_validacion_interpretacion` del ejemplo: **en preparación**
  (se crean después de ejecutar la etapa 6 y las etapas 7 a 9). Hilo de la demo:
  1. **La prueba se abre una sola vez**, con las decisiones ya escritas.
  2. **¿Calibrar?** Se decide con **entidades reservadas**, no con la prueba.
  3. **Intervalo remuestreando entidades** (no filas) y **comparación con el baseline**.
  4. **Matriz de confusión con costos** y **carga de trabajo del analista**: lo que la métrica no ve.
  5. **Errores por segmento** y **SHAP**, con sus límites: *explica al modelo, no al mundo*.
  6. **Atributos sensibles o de uso regulado** entre las variables.
- Hasta que el deck exista, sirve la guía `curso/kit-estudiante/guia-validacion-registro-y-app.md` (secciones 1–4).
- **Preguntas para los grupos:** *¿qué van a escribir como decisión congelada? ¿cómo sabrán si su modelo supera al baseline
  con confianza?*

### 0:40 · Trabajo de grupos — validación e interpretación (55 min)
- Cada grupo trabaja en `notebooks/07_validacion_interpretacion.ipynb` de su repo (esqueleto de la plantilla), con la guía
  y los prompts de la etapa 7.
- Tarea concreta: entrenar el modelo final con todo el entrenamiento, **abrir la prueba una vez**, calcular la métrica
  principal y la de control **con intervalo por entidad** y frente al baseline, hacer **un análisis de errores por segmento
  o de carga de trabajo**, y **una interpretación** (SHAP o importancia por permutación) con su límite.
- **Punto de control 1 (1:30):** ver el punto de control en `lista-de-control.md`. En corto: decisiones **escritas antes** de
  la prueba, prueba abierta **una sola vez** (la marca `reports/prueba_abierta.txt` existe), intervalo por entidad y
  baseline, ≥ 1 análisis de errores o de carga, y una frase sobre el límite de la explicación.
- Un grupo que no llega pasa a apoyo individual durante el descanso; no se bloquea la clase.

### 1:45 · Demo 2 — registro del modelo e inferencia (20 min)
- Diapositivas `05-registro-inferencia-app.md` (parte de registro e inferencia) y notebooks `08_registro_modelo` y
  `09_inferencia` del ejemplo: **en preparación**. Hilo:
  1. **Tracking frente a registro:** ejecuciones (muchas) frente a versiones del modelo (pocas); el **alias `champion`**.
  2. Qué se registra junto al modelo: parámetros, **métricas de la prueba**, **firma**, ejemplo de entrada y etiquetas.
  3. **Nota técnica:** hay que usar `serialization_format="cloudpickle"` al registrar un `Pipeline` (el formato por defecto de
     MLflow lo rechaza), y un *pickle* **puede ejecutar código al cargarse**: solo se cargan modelos propios.
  4. **Ida y vuelta:** cargar desde el registro y comprobar que predice igual.
  5. **Exportar** `models/model.joblib` desde `champion` (la **app no consulta Databricks**) y escribir `input_schema.json`.
  6. **`predict` que valida:** una fila normal, una incompleta y una **imposible** (se niega y explica).
  7. **La ficha del modelo**: qué es, rendimiento con intervalo, límites y usos no recomendados.
- **Preguntas para los grupos:** *¿qué diferencia hay entre su tracking y su registro? ¿qué responde su `predict` con un dato
  imposible?*

### 2:05 · Trabajo de grupos — registrar, exportar y ficha (45 min)
- Cada grupo ejecuta `notebooks/08_registro_modelo.ipynb` y `09_inferencia.ipynb`: registra el modelo con versión y alias,
  comprueba la ida y vuelta, exporta `models/model.joblib` y `models/input_schema.json`, y empieza `models/ficha_modelo.md`
  y `reports/08_registro.md`.
- **Punto de control 2 (2:45):** ver `lista-de-control.md`. En corto: modelo **registrado con versión y alias** (lo ves en
  pantalla), ida y vuelta comprobada, `model.joblib` carga y predice, `input_schema.json` con `valid_range` pensado por el
  grupo (no copiado de los datos) y la ficha del modelo con límites.
- Si Databricks no conecta o la cuota se agotó, `MLFLOW_FORCE_LOCAL=1`: el registro local cuenta igual para H2.

### 2:50 · Demo 3 — módulos con pruebas y esqueleto de la app (20 min)
- Diapositivas `05-registro-inferencia-app.md` (parte de módulos y app), `ejemplo/src/creditsight/inference/` y
  `ejemplo/app/streamlit_app.py`: **en preparación** (la app del ejemplo todavía no se ha probado con un modelo real; la
  **de la plantilla sí** se probó con un modelo de juguete). Hilo:
  1. **La lógica reutilizable vive en `src/`; los notebooks solo orquestan.** Qué ya está en `src/` y qué se añade hoy.
  2. **Pruebas mínimas:** partición por entidad, `predict` que rechaza un dato imposible y acepta uno incompleto, esquema que
     se guarda y se recarga. `tests/test_inference.py` de la plantilla es el modelo (con un modelo de juguete).
  3. **La app de la plantilla:** formulario construido desde el esquema, casilla **"No sé"**, validación, probabilidades y
     aviso de uso responsable. Se ejecuta con `streamlit run app/streamlit_app.py`.
  4. **Qué comprobar:** el formulario aparece, una predicción normal responde, "No sé" no rompe nada y un dato imposible
     muestra un error claro.
- **Preguntas para los grupos:** *¿qué parte de su código sigue viviendo en un notebook? ¿qué prueba protege lo que más puede
  romperse?*

### 3:10 · Trabajo de grupos — módulos, pruebas y app local (35 min)
- Cada grupo pasa a `src/` lo que quede en notebooks, **añade una prueba con una fila de sus datos reales**, ejecuta `pytest`
  y **lanza la app en local** con su modelo.
- Se pide a Claude con el kit, pero con la regla del curso: **revisar el resultado** con
  `kit-estudiante/checklist-revision-ia.md` y **poder explicarlo**. Cambios pequeños, de uno en uno.
- **Punto de control 3 (3:40):** `pytest` **en verde** (con una prueba de inferencia que rechaza datos imposibles) y la **app
  corriendo en local** con su modelo; la ves en pantalla con un dato normal y uno imposible.
- Un grupo sin tiempo termina la app en el trabajo autónomo; lo no negociable es que **haya `pytest` en verde y un
  `model.joblib` que carga**.

### 3:45 · Cierre de H2 y tarea para la clase 5 (15 min)
- **Un minuto por grupo:** su decisión congelada, si su modelo supera al baseline con confianza y el límite principal de su
  modelo. El tiempo se ajusta a la cantidad de grupos del día.
- Revisión de los criterios de **H2** (abajo) y qué falta por grupo.
- **Tarea para mañana (clase 5, viernes 6 de noviembre): llegar listos para desplegar.**
  - `requirements.txt` **en la raíz** del repo, con versiones fijadas y Python 3.12.
  - `models/model.joblib` y `models/input_schema.json` **dentro del repo** y **no ignorados** por `.gitignore`; no subir
    `models/final_pipeline.joblib` (intermedio) ni nada de más de 100 MB.
  - **Cuenta de Streamlit Community Cloud** creada, conectada a su GitHub, y el **repo público** del grupo.
  - Cerrar lo pendiente de H2 y completar `reports/07_validacion.md`, `reports/08_registro.md` y `models/ficha_modelo.md`.
  - Pensar la presentación ejecutiva (máximo 5 diapositivas): problema, enfoque, resultado y costo de negocio, demo y riesgos.

## Criterios de aceptación de H2

Tomados de `specs/001-curso-v2-end-to-end/contracts/etapas.md`:

- **≥ 3 modelos comparados con la misma validación** (ya comprobado en la clase 3).
- **≥ 1 ejecución por candidato registrada** (MLflow local en la clase 3; ya comprobado).
- **Modelo final registrado con versión** (y alias).
- **`src/` con pruebas**: `pytest` en verde.
- **App local que carga el modelo.**

Además, como disciplina del día: **prueba abierta una sola vez**, con decisiones congeladas por escrito antes.

## Qué entrega cada grupo al terminar

| Entregable | Dónde |
|---|---|
| Decisiones congeladas y resultados de la prueba (con intervalo y baseline) | notebook `07` y `reports/07_validacion.md` |
| Marca de apertura de la prueba | `reports/prueba_abierta.txt` |
| Modelo registrado (versión y alias) | Databricks o MLflow local; `reports/08_registro.md` y `reports/08_registro.json` |
| Modelo y esquema exportados | `models/model.joblib` y `models/input_schema.json` |
| Ficha del modelo (iniciada) | `models/ficha_modelo.md` |
| `src/` con pruebas en verde | `src/<paquete>/` y `tests/` |
| App que corre en local | `app/streamlit_app.py` |
| **Sección del reporte** de validación y registro | `reports/` (tercera parte del informe técnico) |

## Reglas de la sesión

- **Las decisiones se escriben antes de abrir la prueba.** Sin decisiones congeladas, no se abre.
- **La prueba se abre una sola vez.** Si se abre otra vez para decidir algo, se declara en el reporte.
- **El intervalo remuestrea entidades, no filas.**
- **La app no consulta Databricks:** carga `models/model.joblib` del repo. **Nada de credenciales en el repo ni en la nube.**
- **El modelo se exporta desde `champion`** y se comprueba que es el que se evaluó.
- **Cada integrante explica lo que generó la IA:** el instructor pregunta a quien no escribió el código.

## Plan B

| Situación | Qué hacer |
|---|---|
| Databricks no conecta (token, perfil, CLI fuera del `PATH`) | `MLFLOW_FORCE_LOCAL=1` en `.env`: el registro local funciona igual y cuenta para H2. `python scripts/verificar_entorno.py` dice qué pasa; la conexión se arregla después |
| Se agotó la cuota diaria de Databricks | Igual: `MLFLOW_FORCE_LOCAL=1`. Los datos de Databricks no se borran; solo no se puede registrar hasta que se renueve la cuota |
| Cómo ver el MLflow local | `mlflow ui --backend-store-uri sqlite:///mlflow_local.db` desde la raíz del repo (ver `curso/guias/databricks-mlflow.md`) |
| `log_model` falla con "untrusted types" | Falta `serialization_format="cloudpickle"` (ver la nota técnica de la guía y del notebook 08) |
| Un grupo **no tiene modelo final decidido** al empezar | Se sienta contigo en la apertura: aplica la regla (optimizados solo si la mejora fue distinguible; el de menor pérdida entre finalistas; el más simple si empatan) y deja el motivo escrito. Si no hay finalistas, se usa el mejor modelo del torneo |
| Un grupo **ya miró la prueba** para decidir | Lo declara por escrito en `reports/07_validacion.md` y reporta la métrica como optimista; si le sobran datos, reserva una nueva partición solo para la comprobación final |
| Un grupo no consigue que la app corra a las 3:40 | Que demuestre `predict_with_scores` en el notebook 09 con una fila normal y una imposible, y que termine la app en el trabajo autónomo (para H3 se necesita) |
| La búsqueda o el SHAP tardan demasiado | SHAP sobre una muestra de unas 400 filas, o importancia por permutación; lo no negociable es una explicación con su límite escrito |

## Lo que el instructor debe tener listo

- [ ] **Etapa 6 ejecutada** y notebooks `07`, `08` y `09` del ejemplo **generados y ejecutados** (hoy **no existen**): sin ellos no hay demos con cifras.
- [ ] Diapositivas `04-validacion-interpretacion.md` y `05-registro-inferencia-app.md` creadas y exportadas a HTML (en preparación).
- [ ] La **app de la plantilla** probada en tu equipo con un modelo real o de juguete (`streamlit run app/streamlit_app.py`).
- [ ] Databricks funcionando para la demo (CLI en el `PATH` o token en `.env`) **y** `MLFLOW_FORCE_LOCAL=1` probado como plan B.
- [ ] `lista-de-control.md` impresa o abierta, con una fila por grupo y los tres puntos de control.
- [ ] Estado de la clase 3 de cada grupo revisado la víspera (repos y reportes `04`, `05` y `06`).
- [ ] Una persona de apoyo para los tres bloques de trabajo (es la clase con más errores de registro y de app).
- [ ] Lista de quién tiene su cuenta de Streamlit Community Cloud lista para mañana (si no, que la creen en el descanso).
