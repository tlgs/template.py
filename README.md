# template.py

A barebones [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python projects.

  - environment management with [direnv](https://direnv.net/)
  - automatic linting/formatting with [pre-commit](https://pre-commit.com/)
  - minimal `README.md`, `pyproject.toml`, and license file
  - support for _src-layout_ and _single-module_ Python distributables,
    as well as collections of miscellaneous scripts

Not all projects require type checking, tests, Sphinx documentation,
or default CI pipelines.

## References

1. [direnv -- Python wiki](https://github.com/direnv/direnv/wiki/Python)
2. [PyPA -- Declaring project metadata (PEP 621 redirect)](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/)
3. [PyPA --  Writing your `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
4. [setuptools -- Popular project layouts](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)
