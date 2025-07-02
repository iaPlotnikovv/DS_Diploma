from pathlib import Path

# Абсолютный путь к корню проекта
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT/"data"
RAW_DATA = DATA_DIR/"raw"
PROCESSED_DATA = DATA_DIR/"processed"
MODELS = PROJECT_ROOT/"model"
