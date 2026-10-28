# Clase 5 · Viernes 6 de noviembre (semana 2) — Despliegue, presentación ejecutiva y ensayo

**Duración:** 4 horas · **Hito del día:** **H3** (app accesible por enlace público, presentación de máximo 5 diapositivas
y ensayo cronometrado de 10 minutos).

> **Calendario del curso.** Seis clases de 4 horas en dos semanas de tres días seguidos: clase 1 (jue 29 oct), clase 2
> (vie 30 oct), clase 3 (sáb 31 oct) · **cinco días de trabajo autónomo** · clase 4 (jue 5 nov), clase 5 (vie 6 nov, hoy) y
> clase 6 (sáb 7 nov). H2 se cerró ayer; hoy se cierra **H3**; **mañana son las exposiciones** y el reporte final (H4) se
> entrega el domingo 15 de noviembre.

## Objetivos

Al terminar la clase, cada grupo tiene:

1. **La app desplegada** en Streamlit Community Cloud, con **enlace público** que abre desde una ventana privada, devuelve
   una predicción coherente con datos válidos y un **error claro** con datos inválidos.
2. **Una presentación ejecutiva de máximo 5 diapositivas**: problema, enfoque, resultado y costo de negocio, demo de la app,
   riesgos y siguientes pasos.
3. **Un ensayo cronometrado de 10 minutos**, con el tiempo real anotado y retroalimentación de otro grupo.
4. **La sección de despliegue del reporte** (`reports/09_despliegue.md`) iniciada, con el enlace de la app.
5. Un **plan B escrito** por si la app falla en vivo mañana (captura de pantalla con fecha y demo en local).

## Cómo se organiza la sesión

Los grupos llegan con **H2 cerrado**: modelo registrado, `models/model.joblib` y `models/input_schema.json` en el repo,
`pytest` en verde y app que corre en local. La clase alterna **tres demos cortas** con **tres bloques de trabajo de grupos** y
termina con **ensayos cronometrados entre grupos**.

| Demo | Máximo | Material |
|---|---|---|
| **1 · Despliegue en Streamlit Community Cloud** | 20 min | `diapositivas/06-despliegue.md` · guía `curso/guias/streamlit-despliegue.md` |
| **2 · La presentación ejecutiva de 5 diapositivas** | 20 min | `diapositivas/07-presentacion-ejecutiva.md` (diap. 1–9) · plantilla `presentacion/ejecutiva.md` |
| **3 · Cómo exponer en 10 minutos** | 10 min | `diapositivas/07-presentacion-ejecutiva.md` (diap. 10–14) · `curso/evaluacion/guia-exposicion.md` |

> **Estado de los materiales de hoy.** La app de **CreditSight (el ejemplo) está pendiente de publicar**: no se ha desplegado
> y los notebooks de las etapas 7 a 9 del ejemplo aún no se ejecutan, así que **no existen las cifras de la prueba** del
> ejemplo. Las diapositivas usan el marcador `[COSTO EN PRUEBA]` donde irá ese dato. **No inventes cifras y no digas que el
> ejemplo está desplegado hasta que lo esté.** Lo que sí está listo: este plan, la lista de control, la guía de los grupos
> (`curso/kit-estudiante/guia-despliegue-y-presentacion.md`), la guía de despliegue, las dos presentaciones y las plantillas de
> `presentacion/ejecutiva.md` y `reports/informe_tecnico.md`.

**No se programa en vivo ni se despliega el ejemplo en vivo:** se recorren los pasos y cada grupo despliega **su** app. Nadie
construye la presentación desde cero: la plantilla trae las cinco diapositivas con sus preguntas.

## Agenda

| Hora | Min | Bloque | Material |
|---|---|---|---|
| 0:00–0:20 | 20 | **Apertura:** estado de H2 y de la app local; revisión previa al despliegue | `lista-de-control.md`, `scripts/verificar_entorno.py` |
| 0:20–0:40 | 20 | **Demo 1:** despliegue en Streamlit Community Cloud | `diapositivas/06-despliegue.md` |
| 0:40–1:30 | 50 | Trabajo de grupos: **despliegue** (**punto de control 1**) | `curso/guias/streamlit-despliegue.md` |
| 1:30–1:40 | 10 | Descanso | — |
| 1:40–2:00 | 20 | **Demo 2:** la presentación ejecutiva de 5 diapositivas | `diapositivas/07-presentacion-ejecutiva.md` |
| 2:00–2:50 | 50 | Trabajo de grupos: **presentación y sección de despliegue del reporte** (**punto de control 2**) | `presentacion/ejecutiva.md`, `reports/09_despliegue.md` |
| 2:50–3:00 | 10 | **Demo 3:** cómo exponer en 10 minutos | `diapositivas/07-presentacion-ejecutiva.md` |
| 3:00–3:45 | 45 | **Ensayos cronometrados** con retroalimentación entre grupos (**punto de control 3**) | `curso/evaluacion/guia-exposicion.md` |
| 3:45–4:00 | 15 | **Cierre de H3** y tarea para la clase 6 | `curso/evaluacion/hitos.md` |

La lista de control del instructor (puntos de control y banco de preguntas orales) está en `lista-de-control.md`.

## Detalle por bloque

### 0:00 · Apertura (20 min)
- **Estado de H2 de cada grupo,** en una hoja visible: ¿`models/model.joblib` y `models/input_schema.json` en el repo?
  ¿`pytest` en verde? ¿la app corre en local? ¿repo **público**? ¿cuenta de Streamlit Community Cloud lista?
- **Revisión previa al despliegue (10 min, cada grupo en su equipo):** `python scripts/verificar_entorno.py` sin `FALTA`,
  `streamlit run app/streamlit_app.py` en local, y comprobar que `requirements.txt` está en la **raíz** y que
  `models/model.joblib` **no** lo ignora el `.gitignore`.
- Quien no tenga modelo exportado o app local se sienta contigo durante la demo 1: no se bloquea la clase, pero **sin app local
  no hay despliegue**. Que use el plan B del plan de la clase 4 (el modelo de la ficha y la app de la plantilla).
- Recuerda la regla de hoy: **mañana expone cada grupo desde su enlace público**; lo que no quede hoy, queda como evidencia local
  con penalización (criterio A3 de la rúbrica).

### 0:20 · Demo 1 — despliegue en Streamlit Community Cloud (20 min)
- Diapositivas `06-despliegue.md` y guía `curso/guias/streamlit-despliegue.md`. Hilo:
  1. **La app no consulta Databricks:** registro → `model.joblib` → repo → app. **Sin credenciales en la nube.**
  2. **Checklist del repo:** repo público, `requirements.txt` en la raíz con versiones fijadas, `model.joblib` dentro del repo y
     no ignorado, app que corre en local.
  3. **Subir a GitHub y comprobar en el navegador** que los archivos aparecen.
  4. **Crear la app** (repo, rama, archivo principal, Python 3.12, *Deploy*). *Verifica los nombres exactos de los botones en la
     documentación oficial; pueden cambiar.*
  5. **Si falla:** los registros (logs) se leen de abajo hacia arriba; los cuatro errores más frecuentes.
  6. **Compartir el enlace:** ventana privada, `README.md`, diapositiva; **abrirla antes de exponer** (las apps pueden dormirse).
- **La app de CreditSight está pendiente de publicar:** no la presentes como desplegada.
- **Preguntas para los grupos:** *¿qué hay en su repo que no debería estar? ¿qué pasa en su app si alguien escribe una edad de
  −500?*

### 0:40 · Trabajo de grupos — despliegue (50 min)
- Cada grupo sigue la guía: ajusta `requirements.txt`, sube `app/`, `models/` y `src/`, crea la app en Streamlit Community Cloud
  y abre el enlace en una **ventana privada**.
- **Punto de control 1 (1:25):** ver `lista-de-control.md`. En corto: **enlace público que abre**, formulario visible, una
  predicción coherente, un dato inválido con **error claro**, sin `.env` ni tokens en el repo, y el enlace pegado en el
  `README.md`.
- Los grupos que no logran desplegar a las 1:25 pasan a **apoyo individual en el descanso**; el que sigue sin enlace a las 2:00
  documenta su **plan de despliegue por escrito** y graba la **captura con fecha** (nivel 1 de A3) mientras sigue intentando.

### 1:40 · Demo 2 — la presentación ejecutiva de 5 diapositivas (20 min)
- Diapositivas `07-presentacion-ejecutiva.md` (diap. 1–9). Hilo:
  1. **Una presentación ejecutiva no es un informe técnico:** una decisión, un número de negocio y un riesgo.
  2. **Las cinco diapositivas:** problema · enfoque · resultado y costo de negocio · demo de la app · riesgos y siguientes pasos.
  3. **De la métrica técnica al lenguaje de negocio** (el resultado va en unidades que entienda quien decide).
  4. **Tres reglas para hablarle a un ejecutivo:** la conclusión primero, un mensaje por diapositiva, cada número con su unidad
     de negocio.
- **Preguntas para los grupos:** *¿cuál es el número que le cambiaría la decisión a su cliente? ¿qué diapositiva sobra?*

### 2:00 · Trabajo de grupos — presentación y sección de despliegue (50 min)
- Cada grupo llena `presentacion/ejecutiva.md` (la plantilla trae **exactamente 5 diapositivas**) con **sus** cifras reales de la
  prueba (`reports/07_validacion.md`) y empieza `reports/09_despliegue.md` con el enlace, las decisiones de despliegue y el plan B.
- Se pide a Claude con el kit, pero con la regla del curso: **revisar el resultado** con `kit-estudiante/checklist-revision-ia.md`
  y **poder explicarlo**.
- **Punto de control 2 (2:45):** ver `lista-de-control.md`. En corto: **máximo 5 diapositivas**, cada una con su mensaje, el
  resultado con **cifra y costo de negocio** (no solo F1 o accuracy), la demo con **tres casos** (normal, límite, inválido) y
  `reports/09_despliegue.md` iniciado.

### 2:50 · Demo 3 — cómo exponer en 10 minutos (10 min)
- Diapositivas `07-presentacion-ejecutiva.md` (diap. 10–14) y `curso/evaluacion/guia-exposicion.md`. Hilo: reparto de tiempos
  **2 · 4 · 3 · 1**, quién habla de qué, el cronómetro (avisos a los 8 y 10 minutos), el plan B de la demo y los errores típicos.

### 3:00 · Ensayos cronometrados (45 min)
- **Formato para cualquier número de grupos:** los grupos se juntan **en parejas**. El grupo A expone (máximo 10 minutos, con
  cronómetro visible); el grupo B toma el tiempo, llena la **hoja de retroalimentación** de `curso/kit-estudiante/guia-despliegue-y-presentacion.md`
  (5 minutos) y se intercambian. Quedan unos **10 minutos** para corregir.
- El ensayo se hace **desde el enlace público**, en un navegador distinto al de desarrollo.
- **Punto de control 3 (3:40):** ver `lista-de-control.md`. En corto: **ensayo completo ≤ 10 minutos con el tiempo real
  anotado**, retroalimentación recibida y **una corrección concreta** que el grupo hizo por ella.
- Tú circulas: escuchas partes sueltas, haces **una pregunta oral** a un integrante distinto de quien habla y anotas en la
  sección de aporte individual.

### 3:45 · Cierre de H3 y tarea para la clase 6 (15 min)
- **Un minuto por grupo:** su enlace, su cifra de negocio y el cambio que harán tras el ensayo. El tiempo se ajusta a la cantidad
  de grupos del día.
- Revisión de los criterios de **H3** (abajo) y qué falta por grupo.
- **Tarea para mañana (clase 6, sábado 7 de noviembre: exposiciones):**
  - Dejar la **app abierta y despierta** al menos 10 minutos antes de exponer, y comprobar el enlace en ventana privada.
  - Tener la **captura de pantalla** y la **app en local** listas como plan B.
  - Decidir **quién habla de cada parte** y quién responde preguntas técnicas (todos deben poder explicar el código de la IA).
  - Corregir la presentación con lo aprendido en el ensayo; **máximo 5 diapositivas**.
  - Avanzar el **reporte técnico** (H4, domingo 15 de noviembre): ya están las secciones de caso, datos, variables, torneo,
    optimización, validación y registro; falta ensamblarlas con el despliegue en `reports/informe_tecnico.md`.

## Criterios de aceptación de H3

Tomados de `curso/evaluacion/hitos.md` y de `specs/001-curso-v2-end-to-end/contracts/etapas.md`:

- **App accesible por enlace público** (se comprueba en una ventana privada).
- **Presentación de máximo 5 diapositivas.**
- **Ensayo de 10 minutos cronometrado.**

Si la app **no se desplegó**, se aplica la penalización de la rúbrica: **máximo nivel 1 en A3**, con evidencia local (captura con
fecha y repo, o demostración en vivo) y el plan de despliegue escrito. No afecta a los demás criterios.

## Qué entrega cada grupo al terminar

| Entregable | Dónde |
|---|---|
| Enlace público de la app | `README.md` del repo y `reports/09_despliegue.md` |
| App y modelo en el repo | `app/streamlit_app.py`, `models/model.joblib`, `models/input_schema.json`, `requirements.txt` en la raíz |
| Presentación ejecutiva (≤ 5 diapositivas) | `presentacion/ejecutiva.md` (y su exportación) |
| Tiempo real del ensayo y retroalimentación | `reports/09_despliegue.md` |
| Plan B (captura con fecha y app en local) | `reports/09_despliegue.md` |
| **Sección del reporte** de despliegue | `reports/09_despliegue.md` (cuarta parte del informe técnico) |

## Reglas de la sesión

- **La app no consulta Databricks:** carga `models/model.joblib` del repo. **Nada de credenciales ni `.env` en el repo ni en la
  nube.** Si Claude propone poner un token «para que funcione», se rechaza.
- **Solo se cargan modelos propios:** un *pickle* puede ejecutar código al cargarse.
- **El enlace se prueba en una ventana privada**, no en la sesión del desarrollador.
- **Cada cifra de la presentación sale de la prueba del grupo** (`reports/07_validacion.md`), con su costo de negocio.
- **Máximo 5 diapositivas y máximo 10 minutos:** se corta a los 10.
- **Cada integrante explica lo que generó la IA:** el instructor pregunta a quien no escribió el código.

## Plan B

| Situación | Qué hacer |
|---|---|
| Streamlit Community Cloud no despliega o no responde | Que lean los registros (guía, apartado 9) y prueben los cuatro errores comunes; si a las 2:00 sigue sin enlace: captura con fecha + plan de despliegue escrito + demo en local (nivel 1 de A3) |
| `ModuleNotFoundError` o error de versión al desplegar | `requirements.txt` incompleto o con versiones distintas de las del entrenamiento; Python 3.12 en *Advanced settings*; commit y push, y la app se reconstruye |
| `FileNotFoundError: models/model.joblib` en la nube | El `.gitignore` lo ignora o la ruta es absoluta; arma la ruta desde la ubicación del archivo (ver la guía) |
| El `model.joblib` pesa demasiado | Un modelo más pequeño (menos árboles) o guardar solo lo que la app necesita; no se suben los datos de entrenamiento (verifica los límites vigentes de GitHub) |
| La app pide un token o falla al conectar | Está llamando a Databricks: se quita esa llamada; la app solo carga `model.joblib` |
| Un grupo **no tiene modelo exportado ni app local** | Se sienta contigo en la apertura: con la plantilla y un modelo de juguete aprende el recorrido, y tu apoyo lo ayuda a exportar el suyo; el despliegue se hace con lo que haya |
| Sin red o Wi-Fi caído | Hotspot; si no hay red, demo en local y capturas; los ensayos se hacen sin enlace público y se anotan como evidencia local |
| La app «duerme» en el ensayo | Abrirla unos minutos antes; en la exposición, abrirla 10 minutos antes de empezar |
| Hay más grupos que tiempo de ensayo | Los ensayos son **por parejas de grupos** en paralelo; tú escuchas solo partes de cada uno |

## Lo que el instructor debe tener listo

- [ ] **Una app desplegada de prueba** (tu propia cuenta de Streamlit Community Cloud) con la plantilla y un modelo de juguete,
      para demostrar los pasos sin sorpresas. **La de CreditSight no está publicada:** no la uses como ejemplo hasta que lo esté.
- [ ] `06-despliegue.md` y `07-presentacion-ejecutiva.md` exportados a HTML y revisados.
- [ ] Una **lista de quién tiene** cuenta de Streamlit Community Cloud y repo público (la de la víspera, de la clase 4).
- [ ] La **hoja de retroalimentación** impresa o abierta (`curso/kit-estudiante/guia-despliegue-y-presentacion.md`) y un cronómetro visible.
- [ ] `lista-de-control.md` abierta, con una fila por grupo y los tres puntos de control.
- [ ] Estado de H2 de cada grupo revisado la víspera (repos y `reports/07_validacion.md`, `08_registro.md`).
- [ ] Una persona de apoyo para los bloques de trabajo (despliegue es donde más se atascan).
- [ ] Wi-Fi probado y un plan B de red (hotspot) para la mañana.
