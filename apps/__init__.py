import os

FILTER = [
    "__init__.py"
]
APPS_DIR = os.path.dirname(__file__)
PY = '.py'

APPS = [file[:-3] for file in os.listdir(APPS_DIR) if file.endswith(PY) and file not in FILTER]
__all__ = ["APPS", *APPS]