"""Post-generation hook

Using `shutil` until Python 3.12 brings `Path.walk`.
"""
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
PROJECT_TYPE = "{{ cookiecutter.project_type }}"


def cleanup_tree() -> None:
    """Re-shape project structure based on type."""
    src_dir = Path("src")

    match PROJECT_TYPE:
        case "single-module":
            (src_dir / PROJECT_SLUG / "__init__.py").replace(PROJECT_SLUG + ".py")
            shutil.rmtree(src_dir)

        case "misc":
            Path("pyproject.toml").unlink()
            shutil.rmtree(src_dir)
            src_dir.mkdir()

    return None


def main() -> int:
    cleanup_tree()
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])

    return 0


if __name__ == "__main__":
    sys.exit(main())
