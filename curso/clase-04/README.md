# Clase 4 · Jueves 5 de noviembre (semana 2)

**Tema:** Validación, registro del modelo y app local · **Hito:** H2

> Calendario: clase 4 es el jueves 5 de noviembre, tras **cinco días de trabajo autónomo** posteriores a la clase 3 (sábado 31
> de octubre). Mañana, clase 5: despliegue y presentación.
>
> **Databricks:** hoy es la **primera vez** que los grupos se conectan para **registrar el modelo final** (alias `champion` en Unity Catalog); en la clase 3 el seguimiento fue local. Plan B: registro local.

## Qué hay en esta carpeta

| Archivo | Para quién | Estado |
|---|---|---|
| [`plan.md`](plan.md) | Instructor | Listo: agenda de 240 min, puntos de control, plan B |
| `lista-de-control.md` | Instructor (solo local, **fuera de Git**) | Listo: hitos, registro por grupo y banco de 20 preguntas orales |
| `diapositivas/04-validacion-interpretacion.md` | Demo 1 | **En preparación** (depende de ejecutar la etapa 6 y de generar y ejecutar las etapas 7–9 del ejemplo, cuyos notebooks aún no existen) |
| `diapositivas/05-registro-inferencia-app.md` | Demos 2 y 3 | **En preparación** (misma dependencia) |
| `notebooks/` | Demo del instructor y esqueletos de los grupos | **En preparación**: se generan con `scripts/sincronizar_notebooks_clase.py` cuando los notebooks `07`–`09` del ejemplo estén ejecutados |

## Material de los grupos (en el kit, fuera de esta carpeta)

- Guía de trabajo: `curso/kit-estudiante/guia-validacion-registro-y-app.md`
- Esqueletos de notebook: `curso/kit-estudiante/plantilla-repo/notebooks/` (`07_validacion_interpretacion`, `08_registro_modelo`, `09_inferencia`)
- Plantillas de reporte y ficha: `reports/07_validacion.md`, `reports/08_registro.md` y `models/ficha_modelo.md` de la plantilla
- Módulos de inferencia y app genérica: `src/proyecto/inference/` (`schema.py`, `predict.py`), `app/streamlit_app.py` y `tests/test_inference.py`

## Pendientes del instructor antes de la clase

1. Ejecutar la etapa 6 (optimización) y después **generar y ejecutar** las etapas 7 a 9 del ejemplo (hoy `ejemplo/notebooks/` solo llega al `06`).
2. Crear las dos presentaciones de las demos con cifras reales.
3. Sincronizar los notebooks de la clase (`python scripts/sincronizar_notebooks_clase.py`).
