"""Copia a cada carpeta de clase los notebooks del ejemplo que se usan en esa clase.

La fuente única de los notebooks del ejemplo es `ejemplo/notebooks/`. Las carpetas de cada clase
(`curso/clase-0N-.../notebooks/demo-instructor/`) reciben una COPIA, con la primera celda ajustada
para que `creditsight` se encuentre desde ahí. Si cambias un notebook del ejemplo, vuelve a ejecutar:

    python scripts/sincronizar_notebooks_clase.py
"""
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ejemplo" / "notebooks"

# carpeta de clase -> notebooks del ejemplo que se muestran en esa clase
CLASES = {
    "clase-02": ["01_caso_negocio", "02_eda", "03_preprocesamiento"],
    "clase-03": ["04_features", "05_torneo"],  # el 06_optimizacion se agrega al ejecutar la etapa 6
    # Se agregan cuando existan las demos: "clase-03": ["04_features", "05_torneo", "06_optimizacion"], ...
}

SETUP = '''import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
# Permite importar `creditsight` sin instalarlo: busca ejemplo/src subiendo desde esta carpeta
for base in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    found = next((c for c in (base / "src", base / "ejemplo" / "src") if (c / "creditsight").exists()), None)
    if found:
        sys.path.insert(0, str(found))
        break
'''


# esqueletos que reciben los estudiantes (fuente: plantilla del kit), copiados SIN cambios
PLANTILLA = ROOT / "curso" / "kit-estudiante" / "plantilla-repo" / "notebooks"
ESQUELETOS = {
    "clase-02": ["02_eda", "03_preprocesamiento"],
    "clase-03": ["04_features", "05_torneo", "06_optimizacion"],
    "clase-04": ["07_validacion_interpretacion", "08_registro_modelo", "09_inferencia"],
}


def main() -> int:
    copied = 0
    for clase, notebooks in ESQUELETOS.items():
        target_dir = ROOT / "curso" / clase / "notebooks" / "plantilla-estudiante"
        target_dir.mkdir(parents=True, exist_ok=True)
        for name in notebooks:
            source = PLANTILLA / f"{name}.ipynb"
            if not source.exists():
                print(f"  FALTA {source.relative_to(ROOT)}")
                continue
            (target_dir / f"{name}.ipynb").write_bytes(source.read_bytes())
            copied += 1
            print(f"  {source.relative_to(ROOT)} -> {(target_dir / (name + '.ipynb')).relative_to(ROOT)}")
    for clase, notebooks in CLASES.items():
        target_dir = ROOT / "curso" / clase / "notebooks" / "demo-instructor"
        target_dir.mkdir(parents=True, exist_ok=True)
        for name in notebooks:
            source = SOURCE / f"{name}.ipynb"
            if not source.exists():
                print(f"  FALTA {source.relative_to(ROOT)}")
                continue
            nb = nbformat.read(source, 4)
            first_code = next(c for c in nb.cells if c.cell_type == "code")
            first_code.source = SETUP
            nbformat.write(nb, target_dir / f"{name}.ipynb")
            copied += 1
            print(f"  {source.relative_to(ROOT)} -> {(target_dir / (name + '.ipynb')).relative_to(ROOT)}")
    print(f"{copied} notebooks sincronizados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
