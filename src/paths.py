import os
import sys
from pathlib import Path

# Универсальная точка входа: работает и в PyInstaller, и в обычной среде
if hasattr(sys, '_MEIPASS'):
    # В режиме PyInstaller: путь к временной распакованной папке
    PROJECT_ROOT = Path(sys._MEIPASS)
else:
    # В режиме обычного Python
    PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA = DATA_DIR / "raw"
PROCESSED_DATA = DATA_DIR / "processed"
MODELS = PROJECT_ROOT / "model"
