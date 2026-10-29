"""Genera (o actualiza) la rama `feature/estudiantes`: lo ÚNICO que se entrega a los estudiantes.

La rama es HUÉRFANA: no comparte historial con `main`. Así, el material del instructor no puede
recuperarse recorriendo el historial de esa rama. (`main` es público: esto da orden, no secreto.)
Se construye desde cero a partir de `main` con una lista de lo que SÍ se entrega; todo lo demás
(specs, planes de clase, banco de preguntas orales, revisión de fichas, credenciales) se queda fuera.

Uso (desde la raíz del repo, con el trabajo de `main` ya commiteado):

    python scripts/publicar_base.py            # crea/actualiza la rama en LOCAL
    python scripts/publicar_base.py --ver      # solo muestra qué contendría, sin tocar Git
    python scripts/publicar_base.py --recrear  # borra la rama local y la crea de nuevo, huérfana

No sube nada a GitHub: el `git push` lo haces tú.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_BRANCH = "feature/estudiantes"

# ---- qué se entrega y dónde queda dentro de la rama base ----
PLANTILLA = ROOT / "curso" / "kit-estudiante" / "plantilla-repo"  # va a la RAÍZ de base
MATERIAL = "material-del-curso"

# (origen relativo a la raíz de main, destino dentro de base, archivos a excluir por nombre)
COPIAS = [
    ("curso/guias", f"{MATERIAL}/guias", set()),
    ("curso/evaluacion", f"{MATERIAL}/evaluacion", {"revision-de-fichas.md"}),  # esta es del instructor
    ("curso/kit-estudiante", f"{MATERIAL}/kit", {"plantilla-repo", "CLAUDE.md", "especificacion-proyecto.md", "LEEME-PRIMERO.md"}),
    ("ejemplo", f"{MATERIAL}/ejemplo-creditsight", {"data_processed", "mlflow_local.db", "mlruns", "models"}),
]
# presentaciones: solo el HTML proyectable de cada clase (no el .md con notas, ni los planes)
PRESENTACIONES = "curso/clase-*/diapositivas/*.html"

# ---- reescritura de rutas dentro de los .md (de rutas de main a rutas de la rama de estudiantes); de lo específico a lo general ----
RUTAS = [
    ("ejemplo/scripts/check_databricks.py", "scripts/check_databricks.py"),
    ("curso/kit-estudiante/especificacion-proyecto.md", "especificacion-proyecto.md"),
    ("curso/kit-estudiante/CLAUDE.md", "CLAUDE.md"),
    ("curso/kit-estudiante/plantilla-repo/", ""),
    ("curso/kit-estudiante/plantilla-repo", "."),
    ("curso/kit-estudiante/", f"{MATERIAL}/kit/"),
    ("curso/kit-estudiante", f"{MATERIAL}/kit"),
    ("curso/guias/", f"{MATERIAL}/guias/"),
    ("curso/guias", f"{MATERIAL}/guias"),
    ("curso/evaluacion/", f"{MATERIAL}/evaluacion/"),
    ("curso/evaluacion", f"{MATERIAL}/evaluacion"),
    ("ejemplo/", f"{MATERIAL}/ejemplo-creditsight/"),
]
IGNORAR = shutil.ignore_patterns("__pycache__", ".ipynb_checkpoints", "*.pyc", ".pytest_cache", "*.db", ".verify-*", "mlruns", "*.pkl", "*.joblib")

# ---- guardas: si algo de esto aparece en lo que se entrega, el script aborta ----
PROHIBIDO_EN_NOMBRE = [r"(^|/)\.env$", r"lista-de-control", r"revision-de-fichas", r"(^|/)specs/", r"(^|/)\.specify/",
                       r"(^|/)\.claude/", r"/plan\.md$", r"(^|/)contrato", r"soluciones", r"^(?!.*/reports/).*\.csv$", r"\.joblib$", r"\.pkl$", r"\.parquet$", r"(^|/)mlruns(/|$)"]
PROHIBIDO_EN_CONTENIDO = [r"ronaldpalencia", r"dbc-[0-9a-f]{8}", r"\bdapi[0-9a-f]{20,}", r"0cd50471", r"banco de preguntas"]
AVISOS_EN_CONTENIDO = [r"PENDIENTE: instructor"]


def git(*args, cwd=ROOT, check=True):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=check).stdout.strip()


def reescribir(texto: str) -> str:
    """Cambia rutas de main por rutas de la rama de estudiantes. El lookbehind evita tocar lo que ya está en formato de base
    (por ejemplo `material-del-curso/guias/` contiene `curso/guias/`)."""
    for viejo, nuevo in RUTAS:
        texto = re.sub(r"(?<![\w/-])" + re.escape(viejo), lambda m, n=nuevo: n, texto)
    return texto


def copiar_arbol(origen: Path, destino: Path, excluir: set) -> None:
    for item in sorted(origen.iterdir()):
        if item.name in excluir or item.name in {"__pycache__", ".ipynb_checkpoints", ".pytest_cache"}:
            continue
        if item.is_dir():
            shutil.copytree(item, destino / item.name, ignore=IGNORAR, dirs_exist_ok=True)
        elif not item.name.endswith((".pyc", ".db")):
            destino.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, destino / item.name)


def construir(destino: Path) -> None:
    # 1) la plantilla del proyecto va a la raíz
    copiar_arbol(PLANTILLA, destino, set())
    # 2) material de consulta
    for origen, dest, excluir in COPIAS:
        copiar_arbol(ROOT / origen, destino / dest, excluir)
    # 3) presentaciones proyectables
    for html in sorted(ROOT.glob(PRESENTACIONES)):
        clase = html.parent.parent.name
        (destino / MATERIAL / "presentaciones" / clase).mkdir(parents=True, exist_ok=True)
        shutil.copy2(html, destino / MATERIAL / "presentaciones" / clase / html.name)
    # 4) texto de bienvenida
    leeme = ROOT / "curso" / "kit-estudiante" / "LEEME-PRIMERO.md"
    if leeme.exists():
        shutil.copy2(leeme, destino / "LEEME-PRIMERO.md")
    # 5) reescribir rutas en los .md y .ipynb de texto
    for archivo in destino.rglob("*.md"):
        if ".git" in archivo.parts:
            continue
        archivo.write_text(reescribir(archivo.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")


def auditar(destino: Path) -> list:
    errores, avisos = [], []
    for archivo in sorted(p for p in destino.rglob("*") if p.is_file() and ".git" not in p.parts):
        rel = archivo.relative_to(destino).as_posix()
        for patron in PROHIBIDO_EN_NOMBRE:
            if re.search(patron, rel):
                errores.append(f"archivo no permitido: {rel}")
        if archivo.suffix.lower() in {".md", ".py", ".json", ".txt", ".yml", ".ipynb", ".html", ".example", ""} or archivo.name.endswith(".env.example"):
            try:
                texto = archivo.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for patron in PROHIBIDO_EN_CONTENIDO:
                if re.search(patron, texto, flags=re.I):
                    errores.append(f"contenido no permitido ({patron}) en {rel}")
            for patron in AVISOS_EN_CONTENIDO:
                if re.search(patron, texto):
                    avisos.append(f"aviso ({patron}) en {rel}")
    return errores, sorted(set(avisos))


def main() -> int:
    solo_ver = "--ver" in sys.argv
    if git("status", "--porcelain"):
        print("AVISO: hay cambios sin commitear en main; la rama se construye desde el árbol de trabajo actual.")
    tmp = Path(tempfile.mkdtemp(prefix="base_"))
    arbol = tmp / "arbol"
    arbol.mkdir()
    construir(arbol)
    errores, avisos = auditar(arbol)
    archivos = sorted(p.relative_to(arbol).as_posix() for p in arbol.rglob("*") if p.is_file())
    print(f"La rama '{BASE_BRANCH}' contendría {len(archivos)} archivos.")
    for a in avisos:
        print("  ", a)
    if errores:
        print("\nERRORES: no se genera la rama.")
        for e in errores:
            print("  ", e)
        shutil.rmtree(tmp, ignore_errors=True)
        return 1
    if solo_ver:
        print("\nPrimer nivel:", sorted({a.split("/")[0] for a in archivos}))
        shutil.rmtree(tmp, ignore_errors=True)
        return 0

    # worktree aparte: no se toca el árbol de trabajo de main
    wt = tmp / "wt"
    existe = bool(git("branch", "--list", BASE_BRANCH))
    if existe and "--recrear" in sys.argv:
        git("branch", "-D", BASE_BRANCH)           # solo la copia local; el remoto no se toca
        existe = False
    if existe and git("merge-base", BASE_BRANCH, "main", check=False):
        print(f"ERROR: '{BASE_BRANCH}' comparte historial con main (no es huérfana). "
              "Ejecuta de nuevo con --recrear para borrarla en local y crearla limpia.")
        shutil.rmtree(tmp, ignore_errors=True)
        return 1
    if existe:
        git("worktree", "add", str(wt), BASE_BRANCH)
    else:
        git("worktree", "add", "--orphan", "-b", BASE_BRANCH, str(wt))
    try:
        for item in wt.iterdir():
            if item.name == ".git":
                continue
            shutil.rmtree(item) if item.is_dir() else item.unlink()
        shutil.copytree(arbol, wt, dirs_exist_ok=True)
        git("add", "-A", cwd=wt)
        if git("status", "--porcelain", cwd=wt):
            origen = git("rev-parse", "--short", "HEAD")
            mensaje = f"Actualiza la rama de estudiantes (generada desde main {origen})"
            subprocess.run(["git", "commit", "-q", "-m", mensaje, "-m", "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"],
                           cwd=wt, check=True, capture_output=True)
            print(f"Rama '{BASE_BRANCH}' actualizada: {git('log', '--oneline', '-1', BASE_BRANCH)}")
        else:
            print(f"Rama '{BASE_BRANCH}' sin cambios.")
    finally:
        git("worktree", "remove", "--force", str(wt), check=False)
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"Para publicarla:  git push -u origin {BASE_BRANCH}   (no se ha subido nada)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
