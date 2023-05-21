import os

FILTER = [
    "__init__.py"
]
TESTCASES_DIR = os.path.dirname(__file__)
PY = '.py'

TESTCASES = [file[:-3] for file in os.listdir(TESTCASES_DIR) if file.endswith(PY) and file not in FILTER]
__all__ = ["TESTCASES", *TESTCASES]