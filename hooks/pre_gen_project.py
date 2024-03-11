"""Pre-generation hook"""

import re
import sys


# valid GitHub repository names (as of Novemeber 2023)
VALID_PATTERN = r"^(?:[\w\-]|[\w\-\.][\w\-]|[\w\-\.]{3,100})$"

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"


def main() -> int:
    print("\n----- PRE  GEN HOOK -----")

    if not re.match(VALID_PATTERN, PROJECT_SLUG):
        print(f'ERROR: "{PROJECT_SLUG}" is not a valid project slug')
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
