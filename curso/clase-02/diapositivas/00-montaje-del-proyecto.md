---
marp: true
theme: default
paginate: true
header: "Casos Avanzados · Maestría en Ingeniería Analítica"
footer: "Clase 2 · Viernes 30 de octubre · Montaje del proyecto (demo ≤ 10 min)"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Montaje del proyecto
## Dejar el repo, el entorno y las conexiones listos

**Clase 2 · Viernes 30 de octubre**

*Demo de ≤ 10 minutos sobre CreditSight. Luego, 40 minutos para montar el suyo.*

<!--
NOTAS DEL PRESENTADOR (demo ≤ 10 min; luego los grupos siguen la guía curso/guias/montaje-proyecto.md)
- Tener abiertos: el repo de ejemplo en VS Code, la guía de montaje y un clon de la rama `base` en una
  carpeta de prueba para ejecutar `verificar_entorno.py` en vivo.
- No instalar nada en vivo: se muestra el resultado y se manda a los grupos a la guía.
-->

---

# 1 · Cómo nace el repositorio del grupo

**No se copian archivos a mano.** El proyecto nace de la rama `base` del curso:

1. **Una persona** crea un repo de GitHub **público y vacío** (sin README).
2. Esa persona clona **solo la rama `base`** y la apunta a su repo:

```bash
git clone --branch base --single-branch https://github.com/palenciaronald/ab-casos-avanzados-2026.git mi-proyecto
cd mi-proyecto
git remote set-url origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git branch -M main
git push -u origin main
```

3. **Los demás** clonan el repo **del grupo**, no el del curso.
4. `material-del-curso/` es de **consulta**: se borra antes de H3 (`git rm -r material-del-curso`).

> Si el repo del grupo **no** estaba vacío, el primer `push` se rechaza: crea uno nuevo y vacío.

<!--
Mostrar los 5 comandos en la terminal con una carpeta de prueba. Insistir en --branch base: `main`
es el curso anterior. Mostrar el LEEME-PRIMERO.md que trae la base.
-->

---

# 2 · El mapa del repositorio

```text
README.md   CLAUDE.md   especificacion-proyecto.md   requirements.txt
.env.example   .gitignore                       ← el .env real NO se sube
data/raw/        datos originales: intocables
data/processed/  datos limpios (los genera el código)
notebooks/       un notebook por etapa; solo orquestan
src/<paquete>/   código reutilizable: data, features, models, tracking, inference
tests/           pruebas con pytest
models/  app/  reports/  presentacion/  scripts/
```

**Ejemplo:** `ejemplo/` (paquete `creditsight`). **Base vacía:** la raíz de la rama `base`.

> *Regla:* la lógica va en `src/`; los notebooks importan de `src/`, nunca al revés.

<!--
Recorrer ejemplo/ en el explorador de VS Code: mostrar src/creditsight/data/cleaning.py y un notebook
(que solo importa y llama). La base trae `src/proyecto/`: cada grupo lo renombra.
-->

---

# 3 · Conexión: `.env` y carpeta de experimentos

Dos formas de conectar a Databricks (**eligen una**; **se prueba hoy y se usa desde la clase 4**):

| Opción | Cuándo | En el `.env` |
|---|---|---|
| **A · Perfil del CLI** | Ya iniciaste sesión con el CLI de Databricks | `PROFILE=<nombre de tu perfil>` |
| **B · Token personal** | Más simple, sin CLI | `DATABRICKS_HOST` y `DATABRICKS_TOKEN` |

- `PYTHONUTF8=1` → evita un error de caracteres en la consola de Windows.
- `EXPERIMENT_DIR=/Users/<tu-correo>/curso_<proyecto>` → carpeta de Databricks (*Workspace → nueva carpeta*)
  donde quedan **todos** los experimentos.
- **El `.env` nunca se sube a GitHub.** Un token en un repo público es un token regalado.
- **Respaldo local:** con `MLFLOW_FORCE_LOCAL=1` el código guarda en un MLflow local y **sigue igual**.

<!--
Mostrar la carpeta real del ejemplo en el workspace y la lista de ejecuciones (si ya se corrió la
optimización del ejemplo). Aclarar que cada cuenta Free Edition es distinta: acuerden hoy qué cuenta
usa el grupo para el seguimiento; los demás pueden trabajar en local.
-->

---

# 4 · La especificación y `CLAUDE.md`

Los dos archivos que **Claude lee antes de escribir una línea**:

| Archivo | Qué dice | Quién lo escribe |
|---|---|---|
| **`especificacion-proyecto.md`** | **Qué** hacemos: caso, datos, unidad de análisis, métrica, riesgos, fechas | El grupo, **a partir de su ficha aprobada** |
| **`CLAUDE.md`** | **Cómo** trabajamos: estructura, estilo, reglas que no se negocian | Viene en el kit; solo se ajusta el nombre del paquete |

**Ejemplo:** `ejemplo/especificacion-proyecto.md` y `ejemplo/CLAUDE.md`.

> Lo que escriban en la especificación **manda** sobre cualquier suposición de la IA.

---

# 5 · `verificar_entorno.py`: verde, amarillo y rojo

```bash
python scripts/verificar_entorno.py
```

| Marca | Significa | Ejemplo |
|---|---|---|
| **OK** | Todo bien | `OK  .env presente y sin valores de ejemplo` |
| **AVISO** | Funciona, conviene revisarlo | `AVISO  Databricks sin configurar: se usará MLflow local` |
| **FALTA** | Hay que arreglarlo antes de seguir | `FALTA  No existe el archivo .env` |

- **No cambia nada** en tu proyecto: solo revisa y da la pista de qué hacer.
- Termina con `Resumen: N OK · N avisos · N por arreglar`.

<!--
Ejecutarlo EN VIVO sobre un clon recién hecho de la rama `base` (saldrán varios FALTA) y volver a
ejecutarlo tras crear el .env: así ven el paso de rojo a verde. Dejar claro que un AVISO de Databricks
NO bloquea.
-->

---

# 6 · Primer commit y push

```bash
git status      # ¿qué se va a subir?
git add .
git commit -m "Montaje inicial del proyecto"
git push
```

**Se sube:** tu proyecto (la base ya viene lista), tu especificación, `CLAUDE.md`, `README.md`.

**NO se sube:**
- `.env` (credenciales) · `.venv/` (tu entorno)
- `data/raw/` con **licencia dudosa o datos personales** (el repo es público)

> Si `.env` aparece en `git status`: **no hagas commit.** Revisa el `.gitignore`.

---

# 7 · Los errores que más van a ver

| Síntoma | Solución rápida |
|---|---|
| **401** de Databricks | Token mal copiado o vencido; host sin `/` final |
| **`databricks` no se reconoce** | No tienen el CLI en el PATH → usar **token** (Opción B) |
| **`UnicodeEncodeError`** (Windows) | `PYTHONUTF8=1` en `.env` |
| **`git push` rechazado** | `git pull --rebase` y luego `git push` |
| **Falla `requirements.txt`** | Python 3.13/3.14 → `uv venv --python 3.12` |

Tabla completa en `curso/guias/montaje-proyecto.md`.

---

# Listo cuando…

- [ ] Repo **público** creado desde la rama `base`; todos clonan el repo **del grupo**
- [ ] Paquete de `src/` con el **nombre de tu proyecto**; `CLAUDE.md` actualizado
- [ ] Entorno con **Python 3.12** y `requirements.txt` instalado
- [ ] `.env` completo y **fuera de Git**
- [ ] Conexión con Databricks **o** acuerdo de usar MLflow local; carpeta de experimentos definida
- [ ] `especificacion-proyecto.md` completa (secciones 1 a 6)
- [ ] Dataset en `data/raw/`, **sin modificar** y sin subir
- [ ] `verificar_entorno.py` con **0 por arreglar** y primer **commit en GitHub**

---

<!-- _class: lead -->
<!-- _paginate: false -->

# A montar el proyecto

**40 minutos.** Sigan `curso/guias/montaje-proyecto.md`.
Cuando tengan las 8 casillas, avisen al instructor.

*Después: EDA.*
