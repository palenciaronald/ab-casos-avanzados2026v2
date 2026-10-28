# Notebooks de la clase 3 (sábado 31 de octubre)

| Carpeta | Para quién | Qué es |
|---|---|---|
| [`demo-instructor/`](demo-instructor/) | **Instructor** | Los notebooks de **CreditSight** ya ejecutados: `04_features` y `05_torneo`. El `06_optimizacion` se agrega cuando se ejecute la etapa 6 |
| [`plantilla-estudiante/`](plantilla-estudiante/) | **Cada grupo** | Los **esqueletos** `04_features`, `05_torneo` y `06_optimizacion`: secciones guía, preguntas y celdas con `TODO`, sin soluciones |

## Fuentes únicas (no edites estas copias)

- Los del instructor salen de [`ejemplo/notebooks/`](../../../ejemplo/notebooks/).
- Los esqueletos salen de [`curso/kit-estudiante/plantilla-repo/notebooks/`](../../kit-estudiante/plantilla-repo/notebooks/).

Para regenerarlas: `python scripts/sincronizar_notebooks_clase.py` (desde la raíz del repo).

## Cómo se usan en la sesión

| Bloque | Notebook |
|---|---|
| 0:20 · Demo 1 (variables) | `demo-instructor/04_features.ipynb` |
| 0:40 · Trabajo de grupos | `plantilla-estudiante/04_features.ipynb` → `notebooks/04_features.ipynb` de su repo |
| 1:40 · Demo 2 (torneo) | `demo-instructor/05_torneo.ipynb` |
| 2:00 · Trabajo de grupos | `plantilla-estudiante/05_torneo.ipynb` → `notebooks/05_torneo.ipynb` |
| 2:50 · Demo 3 (optimización) | `demo-instructor/06_optimizacion.ipynb` *(pendiente de la etapa 6)* |
| 3:10 · Trabajo de grupos | `plantilla-estudiante/06_optimizacion.ipynb` → `notebooks/06_optimizacion.ipynb` |

> Los esqueletos asumen una función `build_pipeline` en `src/<paquete>/models/train.py`. **No viene en la
> plantilla**: cada grupo la crea con Claude (prompts de la etapa 5 en `prompts-por-etapa.md`).
