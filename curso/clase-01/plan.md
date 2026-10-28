# Clase 1 · Jueves 29 de octubre — Nivelación, herramientas y elección de caso

**Duración:** 4 horas · **Entregable del día:** ficha de caso en **borrador** (una por grupo).

## Objetivos

Al terminar la clase 1, cada estudiante:

1. Ve qué parte del curso previo reaparece en su proyecto y sabe en qué puntos tiene vacíos (sin que se los reenseñemos).
2. Maneja el vocabulario del curso: pipeline, proyecto end-to-end, tracking, despliegue.
3. Tiene su entorno instalado y la conexión probada (o un plan B documentado).
4. Conoce la rúbrica y el kit de trabajo con Claude.
5. Pertenece a un grupo que ya tiene una ficha de caso en borrador.

> **Principio del curso.** No se repite lo que ya vieron. El diagnóstico sirve para **detectar
> vacíos y orientar**, no para dar clase.

## Agenda

| Hora | Min | Bloque | Material |
|---|---|---|---|
| 0:00–0:10 | 10 | Bienvenida: qué es el curso, seis clases en dos semanas, entregables y hitos | `curso/clase-01/diapositivas/bienvenida-y-cierre.md` (diapositivas 1–7) |
| 0:10–0:30 | 20 | **Mapa de lo visto** en el curso previo | `curso/clase-01/diapositivas/mapa-curso-previo.md` |
| 0:30–1:05 | 35 | **Diagnóstico** (12 preguntas, sin nota) | `curso/clase-01/diapositivas/diagnostico.md` |
| 1:05–1:20 | 15 | Lectura de resultados y **formación de grupos** | `curso/clase-01/diapositivas/eleccion-de-caso.md` (diapositiva "Los grupos") |
| 1:20–2:00 | 40 | **Nivelación** conceptual: pipeline, end-to-end, tracking, despliegue | `curso/clase-01/diapositivas/nivelacion.md` |
| 2:00–2:10 | 10 | Descanso | — |
| 2:10–2:30 | 20 | **Tecnologías** del curso | `curso/clase-01/diapositivas/tecnologias.md` |
| 2:30–3:05 | 35 | **Instalación guiada** + prueba de conexión (en grupos) | `curso/guias/instalacion.md` |
| 3:05–3:20 | 15 | **Publicar la rúbrica** y **presentar el kit** | `curso/clase-01/diapositivas/rubrica-y-kit.md`, `curso/evaluacion/rubrica.md`, `curso/kit-estudiante/` |
| 3:20–3:55 | 35 | **Elección del caso** y ficha | `curso/clase-01/diapositivas/eleccion-de-caso.md`, `curso/evaluacion/criterios-dataset.md`, `curso/evaluacion/ficha-de-caso.md` |
| 3:55–4:00 | 5 | Cierre y tarea | `curso/clase-01/diapositivas/bienvenida-y-cierre.md` (diapositivas 8–10) |

> **Por qué este orden.** Primero lo conocido (mapa y diagnóstico), después **los grupos**, que se
> forman con el resultado del diagnóstico para que cada uno tenga una persona fuerte en cada tema.
> Luego lo nuevo (nivelación y herramientas), la instalación **en grupos** (quien ya tiene su
> entorno ayuda a los demás) y, al final, lo práctico: rúbrica, kit y elección del caso. Las
> herramientas van **antes** del caso para que el grupo conozca sus límites al elegir los datos
> (Databricks, Streamlit y Claude).

## Detalle por bloque

### 0:00 · Bienvenida (10 min)
- Calendario: seis clases de 4 horas en dos semanas (jueves 29, viernes 30 y sábado 31 de octubre; jueves 5,
  viernes 6 y sábado 7 de noviembre), 24 horas presenciales. Entre la clase 3 y la clase 4 hay 5 días de trabajo autónomo.
- Entregables del grupo: repositorio modular, notebooks, modelo final, reporte técnico, presentación
  de máximo 5 diapositivas y app desplegada. Exposición de máximo 10 minutos en la clase 6 (sábado 7 de noviembre).
- Hitos con fecha: H1 (cierre de la clase 2, viernes 30 de octubre), H2 (clase 4, jueves 5 de noviembre), H3 (clase 5, viernes 6 de
  noviembre) y H4 (domingo 15 de noviembre) (`curso/evaluacion/hitos.md`).

### 0:10 · Mapa de lo visto (20 min)
- Se proyecta `mapa-curso-previo.md`: **13 diapositivas**, una por tema del curso previo, cada una
  con *lo que recuerdas*, *la trampa* y *aquí lo usarás* en el proyecto.
- Ritmo: ~1,5 minutos por diapositiva. **No se reenseña**: si preguntan "¿puedes explicar X?", se
  responde "está en la sesión correspondiente; hoy solo ubicamos dónde reaparece".
- Cierre del bloque: la diapositiva **"Lo que NO vieron"** (seguimiento de experimentos, servir y
  desplegar un modelo). Es el puente hacia la nivelación y justifica el curso.

### 0:30 · Diagnóstico (35 min)
- Se proyecta `diagnostico.md`: **12 preguntas**, cada una con su respuesta en la diapositiva
  siguiente. Los estudiantes responden primero por escrito y comparan después.
- **Regla del instructor:** se muestra la respuesta, se hace una aclaración de **un minuto** como
  máximo y se sigue. Si hay muchas fallas en un tema, se anota; no se detiene la sesión.
- Si el ritmo se atrasa, se recorta a las 8 preguntas más relevantes para el curso (fuga,
  validación por grupo, desbalance/umbral, calibración, pipeline).

### 1:05 · Lectura de resultados y formación de grupos (15 min)
- Cada estudiante identifica sus 2–3 vacíos mayores con la tabla de lectura del diagnóstico.
- El instructor propone **apoyo fuera de clase** (el material del curso previo, la guía del kit),
  no clase extra. **Los grupos se arman ahora** (tamaño y número los define el instructor según la asistencia; roles: datos, modelado, app y negocio) y conviene que cada grupo tenga al menos una
  persona fuerte en cada tema que apareció como vacío frecuente.

### 1:20 · Nivelación (40 min)
- Se proyecta `nivelacion.md` (CreditSight como hilo conductor): pipeline, proyecto end-to-end,
  tracking de modelos y despliegue.
- La diapositiva de **tracking** parte del problema *"¿cuál de las 30 pruebas de ayer era la
  buena?"*. Pedir a los estudiantes que cuenten cómo lo resuelven hoy.
- Pregunta de cierre: *¿qué parte del proyecto les parece más difícil de hacer solos?* Anotar las
  respuestas: orientan las demos de las clases 3 y 4.

### 2:10 · Tecnologías (20 min)
- Se proyecta `tecnologias.md`: Python con `.venv`, Git y GitHub, VS Code con la extensión de Claude
  Code, Databricks Free Edition, MLflow y Streamlit.
- Para cada herramienta se dice **qué NO tienen que dominar**. Se recuerda que usarán Claude como
  asistente obligatorio (plan individual de pago si no lo tienen) y la sección de cuota en
  `curso/guias/desarrollo-con-ia.md`.

### 2:30 · Instalación guiada, en grupos (35 min)
- Cada estudiante sigue `curso/guias/instalacion.md` en su equipo. El instructor y un apoyo
  circulan.
- **Meta mínima de la prueba:** crear el entorno, completar `.env` y ejecutar
  `python ejemplo/scripts/check_databricks.py` con resultado "OK".
- Anotar en una lista visible quién queda **pendiente** y por qué (ver plan B).

### 3:05 · Rúbrica y kit (15 min)
- **Rúbrica** (`curso/evaluacion/rubrica.md`): recorrerla criterio por criterio, sin entrar en
  detalle de ponderación (está en la tabla de la rúbrica). Subrayar la regla del curso: *cada integrante debe
  poder explicar el código que la IA generó*, y que habrá una pregunta oral.
- **Kit** (`curso/kit-estudiante/`): mostrar `CLAUDE.md`, la plantilla de especificación del
  proyecto, los prompts por etapa y la lista de revisión del código generado. Decir de dónde sale: viene en la
  raíz de la rama `base`, que cada grupo clona una vez y apunta a su repositorio (ver `LEEME-PRIMERO.md`); la IA lo lee antes de generar nada.

### 3:20 · Elección del caso y ficha (35 min)
Se proyecta `eleccion-de-caso.md` (**15 diapositivas**: se proyectan hasta "La ficha de caso" y la lista rápida y el cierre quedan de apoyo).

1. **Criterios de dataset** (5 min): se proyecta `criterios-dataset.md`. Recordar que **no** valen
   los datasets de clase ni los del curso previo, ni los del ejemplo, y que los datos del trabajo
   solo si no son confidenciales.
2. **Elegir y escribir la ficha** (30 min): cada grupo diligencia la plantilla de
   `curso/evaluacion/ficha-de-caso.md` con `status: borrador`. Tomar como modelo el ejemplo de
   CreditSight (`ejemplo/reports/00_caso.md`).
- El instructor recorre los grupos y filtra de inmediato: dataset trivial, objetivo ambiguo, sin
  costo de equivocarse definible.

### 3:55 · Cierre (5 min)
- **Tarea:** completar y corregir la ficha; dejar el repositorio del grupo creado (una persona lo crea
  vacío, clona la rama `base` y la apunta al repo del grupo) y compartir el enlace.
- **Mañana:** la ficha se aprueba o se devuelve en la primera media hora.

## Plan B si la instalación falla

| Situación | Qué hacer |
|---|---|
| El equipo no deja instalar (equipo corporativo) | Trabajar **en pareja** con un compañero cuyo entorno funcione; la persona sin entorno participa en EDA y decisiones y avisa al instructor |
| Databricks no conecta (token, perfil, cuota) | Poner `MLFLOW_FORCE_LOCAL=1` en `.env`: el código usa MLflow local y el curso continúa; la conexión se arregla antes de la clase 3 (sábado 31 de octubre) |
| El CLI de Databricks no está en el `PATH` | Cambiar a la **opción B** (host y token personal) del `.env.example`, que no requiere el CLI |
| Error de codificación en consola de Windows | Definir `PYTHONUTF8=1` en `.env` (está en la sección de errores comunes de la guía) |
| No tiene plan de Claude | Seguir la política de respaldo de `curso/guias/desarrollo-con-ia.md` y avisar al instructor hoy |
| Quedan más de 5 personas sin entorno al final del bloque | Dejar de instalar en grupo; el instructor abre una **sesión de apoyo** antes de la clase 2 (viernes 30 de octubre) y se sigue con los grupos |

> **Criterio para no bloquear a todos:** la instalación nunca debe consumir más del bloque
> asignado. Lo que no se resuelva a las 3:05 pasa a apoyo individual.

## Entregable del día

- Ficha de caso en `borrador` por grupo (`reports/00_caso.md` del repo del grupo).
- Lista de pendientes de instalación con responsable.
- Lista de vacíos frecuentes detectados en el diagnóstico (insumo para la clase 3).

## Lo que el instructor debe tener listo

- [ ] `mapa-curso-previo`, `diagnostico`, `nivelacion`, `tecnologias` y `eleccion-de-caso` revisados y exportados a HTML.
- [ ] Rúbrica publicada y accesible para todos.
- [ ] La rama `base` publicada en GitHub y su enlace listo para compartir (`LEEME-PRIMERO.md` explica cómo clonarla).
- [ ] Un apoyo para la instalación (otra persona o un grupo avanzado).
- [ ] Ejemplo de CreditSight abierto (`ejemplo/reports/00_caso.md`).
