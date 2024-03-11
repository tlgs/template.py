"""Post-generation hook"""

import shutil
import sys
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT


PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
PROJECT_TYPE = "{{ cookiecutter.project_type }}"


def cleanup_tree() -> None:
    """Re-shape project structure based on type."""
    src_dir = Path("src")

    match PROJECT_TYPE:
        case "package":
            pass

        case "single-module":
            (src_dir / PROJECT_SLUG / "__init__.py").replace(PROJECT_SLUG + ".py")
            shutil.rmtree(src_dir)

        case "bare":
            Path("pyproject.toml").unlink()
            shutil.rmtree(src_dir)

        case _:
            raise ValueError(f"Invalid {PROJECT_TYPE=}")

    return None


def run(*args, direnv=False):
    """Wrapper around subprocess.Popen to inject arguments and process output."""
    if direnv:
        args = ("direnv", "exec", ".", *args)

    quoted_args = [f"'{arg}'" if " " in arg else arg for arg in args]
    print("\n$ ", " ".join(quoted_args), sep="")

    with Popen(args, stdout=PIPE, stderr=STDOUT) as proc:
        for line in proc.stdout:
            print("  ", line.decode(), sep="", end="")


def main() -> int:
    print("----- POST GEN HOOK -----")

    cleanup_tree()

    run("git", "init")
    run("python", "-c", "import sys; print(sys.executable)", direnv=True)
    run("pip", "install", "pre-commit", direnv=True)
    run("pre-commit", "install", direnv=True)
    run("pre-commit", "autoupdate", direnv=True)
    run("git", "add", ".")

    return 0


if __name__ == "__main__":
    sys.exit(main())
