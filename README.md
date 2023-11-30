# template.py

A barebones [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python projects.

  - bare `README.md` and `UNLICENSE`
  - [direnv](https://github.com/direnv/direnv)-based setup
    (stock `.envrc` and `.gitignore`)
  - minimal `pre-commit`
    and [`pyproject.toml`](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use)
    configuration
  - support for _src-layout_ and _single-module_ Python distributables,
    as well as collections of miscellaneous scripts

Not all projects require type checking, tests, Sphinx documentation,
or default CI pipelines.
