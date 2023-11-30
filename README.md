# template.py

A barebones [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python projects.

  - [direnv](https://github.com/direnv/direnv)-based setup
  - minimal `pre-commit`
    and [`pyproject.toml`](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use)
    configuration
  - bare `README.md` and `UNLICENSE`
    (stock `.envrc` and `.gitignore`)
  - support for _src-layout_ and _single-module_ Python distributables,
    as well as collections of miscellaneous scripts

Not all projects require type checking, tests, Sphinx documentation,
or default CI pipelines.
