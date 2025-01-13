import os
import sys
from pathlib import Path
from cx_Freeze import setup, Executable

# ---------------------------------------------------
# 사용자 설정
# ---------------------------------------------------
exe_name = "PyDracula"
version = "1.01"

# ---------------------------------------------------
# 프로젝트 경로 설정
# ---------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------
# 소스 경로 및 주요 파일 설정
# ---------------------------------------------------
SRC_DIR = PROJECT_ROOT / 'src'
MAIN_PY = SRC_DIR / 'main.py'
ASSETS_DIR = SRC_DIR / 'assets'
CONFIG_DIR = SRC_DIR / 'config'

# ---------------------------------------------------
# 포함할 파일/폴더
# (현 위치 , 옮길 위치)
# ---------------------------------------------------
files = [
    ('icon.ico','icon.ico'),
    ('themes/','themes/'),
    (str(ASSETS_DIR),'assets/'),
    (str(CONFIG_DIR),'config/')
]
# ---------------------------------------------------
# 버전 및 빌드 폴더 설정
# ---------------------------------------------------

build_folder = PROJECT_ROOT / "release" / version

# ---------------------------------------------------
# 제외할 라이브러리
# ---------------------------------------------------
excludes = ['tkinter']

# ---------------------------------------------------
# 포함할 패키지
# (다른 환경에서 실행하기 위해 필요한 것들)
# ---------------------------------------------------
packages = [
    'PySide6.QtCore',
    'PySide6.QtGui',
    'PySide6.QtWidgets'
]

# ---------------------------------------------------
# 실행 파일(target) 설정
# ---------------------------------------------------
platform_base = "Win32GUI" if sys.platform == "win32" else None

target = Executable(
    script=str(MAIN_PY),
    base=platform_base,
    icon=str(PROJECT_ROOT / "icon.ico"),
    target_name = f"{exe_name}_{version}.exe",
)

# ---------------------------------------------------
# setup() 설정
# ---------------------------------------------------
setup(
    name=exe_name,
    version=version,
    description="Modern GUI for Python applications",
    author="jonus",  # 필요 시 변경
    options={
        'build_exe': {
            'include_files': files,
            'build_exe': str(build_folder),
            'excludes': excludes,
            'packages': packages,
            'optimize': 2  # 최적화 레벨, 필요 시 조정
        }
    },
    executables=[target]
)
