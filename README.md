# template.py

A barebones [cookiecutter](https://www.cookiecutter.io/) template for Python projects.

  - environment management with [direnv](https://direnv.net/)
  - automatic linting/formatting with [pre-commit](https://pre-commit.com/)
    and [Ruff](https://docs.astral.sh/ruff/)
  - minimal `pyproject.toml` configuration
  - support for _src-layout_ and _single-module_ Python distributables,
    as well as a bare repository

Not all projects require type checking, tests, Sphinx documentation,
or default CI pipelines.

## Usage

```
cookiecutter gh:tlgs/template.py
```

## References

1. [direnv -- Python wiki](https://github.com/direnv/direnv/wiki/Python)
2. [PyPA -- `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
3. [PyPA --  Writing your `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
4. [setuptools -- Popular project layouts](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)
