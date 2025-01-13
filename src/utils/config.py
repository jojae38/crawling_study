from pathlib import Path
from utils.toolbox import create_folder
import sys

if getattr(sys, "frozen", False):  # cx_Freeze로 실행된 경우
    PROJECT_ROOT = Path(sys.executable).resolve().parent
    print(rf"패키징 된 실행 환경 : {PROJECT_ROOT}")
else:  # 개발 환경에서 실행된 경우
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    print(rf"개발 환경 : {PROJECT_ROOT}")

DIRS_DICT = {
    'ASSETS_DIR': PROJECT_ROOT / 'assets',
    'LOG_DIR': PROJECT_ROOT / 'logs',
}

for DIR in DIRS_DICT.values():
    create_folder(DIR)