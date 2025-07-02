import sys
from pathlib import Path

def path_setup():
    project_root = Path.cwd().parent
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root))