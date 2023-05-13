import os

FILTER = [
    "__init__.py"
]
SRCS_DIR = os.path.dirname(__file__)
PY = '.py'

SRCS = [file[:-3] for file in os.listdir(SRCS_DIR) if file.endswith(PY) and file not in FILTER]
__all__ = ["SRCS", *SRCS]