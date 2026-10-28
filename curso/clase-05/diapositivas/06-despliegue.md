---
marp: true
theme: default
paginate: true
header: "Casos Avanzados · Maestría en Ingeniería Analítica"
footer: "Clase 5 · Viernes 6 de noviembre · Demo 1: despliegue en Streamlit Community Cloud (20 min)"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# De la app local a un enlace público
## Desplegar en Streamlit Community Cloud

**Clase 5 · Viernes 6 de noviembre**

<!--
NOTAS DEL PRESENTADOR (demo de 20 min; ~12 diapositivas)
- Los pasos se recorren, no se programan en vivo. Cada grupo despliega SU app en el bloque siguiente (50 min).
- La app de CreditSight (el ejemplo) está PENDIENTE DE PUBLICAR: no la presentes como desplegada. Si quieres mostrar el
  recorrido en pantalla, usa tu app de prueba con la plantilla y un modelo de juguete.
- No inventes nombres de botones: "verifica en la documentación oficial de Streamlit; pueden cambiar".
-->

---

# Qué vamos a lograr hoy

- Pasar de **«corre en mi computador»** a **un enlace que abre cualquiera**.
- Hacerlo **sin poner credenciales** en la nube.
- Dejar la app **lista para exponer mañana**.

**Punto de control 1:** el enlace abre en una **ventana privada**, muestra el formulario, predice un caso conocido y
rechaza un dato inválido con un mensaje claro.

> Mañana cada grupo expone **desde su enlace público**. Si no hay enlace, la rúbrica da como máximo el nivel 1 de A3, con
> evidencia local.

<!--
Recuérdales la penalización de A3 sin dramatizar: es una consecuencia clara y conocida desde la clase 1.
-->

---

# La app **no consulta Databricks**

```text
Databricks (registro del modelo, fuente de verdad)
        │  exportas la versión champion
        ▼
models/model.joblib  ──►  tu repo público  ──►  tu app en la nube
```

- La nube **no tiene** tu token ni tu sesión de Databricks, y **no debes ponerlos allí**.
- Lo que subes a un repo público lo ve **cualquiera**.
- Además la app **no debe depender** de la cuota diaria de la plataforma.

> **Regla:** si algo te pide un token «para que funcione», la respuesta es **no**: se quita esa llamada.

---

# Antes de desplegar: el repo

| Requisito | Por qué |
|---|---|
| Repo **público** en GitHub | Streamlit lo lee desde GitHub |
| `requirements.txt` en la **raíz** | Ahí lee las librerías que debe instalar |
| `models/model.joblib` **dentro** del repo | La app carga el modelo de ese archivo |
| La app **corre en local** | Si no corre en tu computador, no correrá en la nube |
| Sin `.env` ni datos personales | Todo lo público lo puede ver cualquiera |

```bash
streamlit run app/streamlit_app.py     # compruébalo primero en local
```

---

# `requirements.txt`: la raíz y las versiones

- Va en la **raíz** del repo (no dentro de `app/`).
- Lista **solo lo que la app necesita**, con versiones fijadas: `nombre==versión`.
- Usa **las mismas versiones con las que entrenaste** (sobre todo `scikit-learn`, `lightgbm`, `xgboost`, `pandas`,
  `joblib`): un modelo guardado con una versión puede fallar con otra.
- Python **3.12**, la misma de tu entorno.

> ¿No sabes qué librerías hacen falta? Pídele a Claude: *«revisa `app/streamlit_app.py` y `src/` y dime qué necesito en
> `requirements.txt`»*. Y **revisa** lo que responda.

---

# Tamaño y `.gitignore`: dos causas de «no aparece mi modelo»

- **El `.gitignore` lo ignora** (una regla `*.joblib` o `models/`): el archivo existe en tu computador pero **no en
  GitHub**. Quita la regla solo para `models/model.joblib`.
- **No subas** `models/final_pipeline.joblib` (intermedio y pesado) ni los **datos de entrenamiento**: la app no los necesita.
- Si `model.joblib` es muy grande: un modelo más pequeño (menos árboles) o guardar solo lo que la app necesita.
  *Verifica los límites vigentes de GitHub en su documentación.*

```bash
ls -lh models/          # macOS/Linux; en Windows, propiedades del archivo
```

---

# Subir a GitHub y comprobar en el navegador

```bash
git add app/ models/ src/ requirements.txt
git commit -m "App lista para desplegar"
git push
```

Después, **en el navegador**, entra a tu repo y comprueba que **sí aparecen**:

☐ `models/model.joblib`   ☐ `requirements.txt`   ☐ `app/streamlit_app.py`   ☐ `models/input_schema.json`

> Si algo no aparece, **no sigas**: revisa el `.gitignore` antes de crear la app.

---

# Crear la app en Streamlit Community Cloud

1. Entra a **Streamlit Community Cloud** (búscalo en su documentación oficial) con tu cuenta de **GitHub**.
2. **Crear una app** nueva y elegir el **repo**, la **rama** y el **archivo principal**:
   - En el repo del grupo: `app/streamlit_app.py`.
3. En la **configuración avanzada**, elegir **Python 3.12**.
4. **Deploy.** La primera vez tarda unos minutos: instala las librerías.

> *Verifica en la documentación oficial los nombres exactos de los botones y las condiciones vigentes de la versión gratuita;
> pueden cambiar.*

<!--
La app de CreditSight está PENDIENTE DE PUBLICAR. Si preguntan "¿dónde está el ejemplo?", dilo así, sin inventar un enlace.
-->

---

# Si falla: lee los registros (logs)

**De abajo hacia arriba:** la última línea suele decir qué falló.

| Síntoma | Causa probable |
|---|---|
| `ModuleNotFoundError` | Falta una librería en `requirements.txt` |
| `FileNotFoundError: models/model.joblib` | No se subió, o la ruta es absoluta |
| Error al cargar el modelo (versión) | Versiones distintas de las del entrenamiento |
| Funciona en local y no en la nube | Distinta versión de Python |

Cada `git push` **reconstruye** la app solo. **Espera** a que termine antes de probar.

> Regla de oro: si no lo entiendes, **copia el mensaje completo a Claude** y dile en qué paso estabas.

---

# Compartir el enlace (y que esté despierta)

- **Ábrelo en una ventana privada:** debe verlo alguien sin tu sesión.
- **Pégalo** en el `README.md`, en la diapositiva de la app y en `reports/09_despliegue.md`.
- Las apps pueden **dormirse** si no se usan: **ábrela unos minutos antes** de exponer
  *(verifica las condiciones vigentes en la documentación oficial)*.
- Comprueba **tres casos**: uno normal, uno límite y uno **inválido** (que debe rechazarse con un mensaje claro).

---

# Plan B: si el despliegue no sale

| Qué | Cómo |
|---|---|
| **Evidencia local** | App corriendo en local + **captura de pantalla con fecha y repo** |
| **Plan de despliegue escrito** | Qué intentaron, qué error dio y qué harían |
| **Rúbrica (A3)** | **Nivel máximo 1.** No afecta a los demás criterios |

Y lo importante: **no se detiene el resto del día.** Mientras siguen intentando, avanzan con la presentación.

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Punto de control 1
## Enlace público · formulario visible · caso válido · dato inválido rechazado

☐ Sin `.env`, token ni datos personales en el repo
☐ Enlace pegado en el `README.md`

**Ahora, a desplegar: 50 minutos.**
