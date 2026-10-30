# Notebooks de la clase 2 (viernes 30 de octubre)

Dos juegos, para dos personas distintas:

| Carpeta | Para quién | Qué es |
|---|---|---|
| [`demo-instructor/`](demo-instructor/) | **Instructor** | Los notebooks de **CreditSight** ya ejecutados, con sus resultados: `01_caso_negocio`, `02_eda` y `03_preprocesamiento`. Se recorren en las demos A, B y C; **no se programa en vivo** |
| [`plantilla-estudiante/`](plantilla-estudiante/) | **Cada grupo** | Los **esqueletos** `01_caso_negocio`, `02_eda` y `03_preprocesamiento`: secciones guía, preguntas y celdas con `TODO`, sin ninguna solución. Los grupos los llenan con **su** dataset |

## Fuentes únicas (no edites estas copias)

- Los notebooks del instructor salen de [`ejemplo/notebooks/`](../../../ejemplo/notebooks/).
- Los esqueletos salen de la plantilla del kit: [`curso/kit-estudiante/plantilla-repo/notebooks/`](../../kit-estudiante/plantilla-repo/notebooks/).

Si cambias uno de los originales, regenera estas copias desde la raíz del repo:

```bash
python scripts/sincronizar_notebooks_clase.py
```

## Cómo se usan en la sesión

| Bloque | Notebook |
|---|---|
| 1:10 · Demo A (caso de negocio) | `demo-instructor/01_caso_negocio.ipynb` |
| 1:20 · Trabajo de grupos | `plantilla-estudiante/01_caso_negocio.ipynb` → `notebooks/01_caso_negocio.ipynb` de su repo |
| 1:35 · Demo B (EDA) | `demo-instructor/02_eda.ipynb` |
| 1:55 · Trabajo de grupos | `plantilla-estudiante/02_eda.ipynb` → `notebooks/02_eda.ipynb` de su repo |
| 2:45 · Demo C (preprocesamiento y fuga) | `demo-instructor/03_preprocesamiento.ipynb` |
| 3:05 · Trabajo de grupos | `plantilla-estudiante/03_preprocesamiento.ipynb` → `notebooks/03_preprocesamiento.ipynb` de su repo |

> El montaje del proyecto (primer bloque) **no usa notebook**: es la guía `curso/guias/montaje-proyecto.md`
> y el script `scripts/verificar_entorno.py`.
