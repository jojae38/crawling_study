from pathlib import Path
from utils.toolbox import create_folder, read_json
import sys

if getattr(sys, "frozen", False):  # cx_Freeze로 실행된 경우
    PROJECT_ROOT = Path(sys.executable).resolve().parent
    print(f"패키징 된 실행 환경: {PROJECT_ROOT}")
    print(f"실행 파일 경로: {sys.executable}")
else:  # 개발 환경에서 실행된 경우
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    print(f"개발 환경: {PROJECT_ROOT}")
    print(f"Python 인터프리터 경로: {sys.executable}")

# import json

# JSON 파일에서 경로 읽기
# with open(PROJECT_ROOT / 'config' /'path.json') as f:
#     DIRS_CONFIG = json.load(f)
DIRS_CONFIG = read_json(PROJECT_ROOT / 'config' /'path.json')

# DIRS_DICT = {
#     'ASSETS_DIR': PROJECT_ROOT / 'assets',
#     'LOG_DIR': PROJECT_ROOT / 'logs',
# }
DIRS_DICT = {key: PROJECT_ROOT / value for key, value in DIRS_CONFIG.items()}

for DIR in DIRS_DICT.values():
    create_folder(DIR)