import os
from pathlib import Path
from cx_Freeze import setup, Executable

PROJECT_ROOT = Path(__file__).resolve().parent

SRC_DIR = PROJECT_ROOT / 'src'
MAIN_PY = SRC_DIR / 'main.py'
ASSETS_DIR = SRC_DIR / 'assets'
CONFIG_DIR = SRC_DIR / 'config'

print(PROJECT_ROOT)
build_folder = os.path.join(PROJECT_ROOT, "release", "1.0")

# 아이콘이랑 테마는 프로젝트 파일 내부에 둘 것!
files = ['icon.ico','themes/']


# EXCLUDES
excludes = ['tkinter']

# INCLUDE PACKAGES - 다른 환경에서 실행시키려면 필요함
packages = ['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets']

# 나머지 설정은 동일
setup(
    name="PyDracula",
    version="1.0",
    options={
        'build_exe': {
            'include_files': files,
            'build_exe': build_folder,
        }
    },
    executables=[
        Executable(
            script=MAIN_PY,
            base="Win32GUI",
            icon=os.path.join(PROJECT_ROOT, "icon.ico"),
            target_name="PyDracula.exe",
        )
    ]
)
# # ADD FILES
# files = ['icon.ico','themes/']

# # VERSION
# version = "1.0"
# build_folder = f"release/{version}"

# # EXCLUDES
# excludes = ['tkinter']

# # INCLUDE PACKAGES - 다른 환경에서 실행시키려면 필요함
# packages = ['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets']

# # TARGET
# target = Executable(
#     script="main.py",
#     base="Win32GUI",
#     icon="icon.ico",
#     target_name="PyDracula.exe",
# )

# # SETUP CX FREEZE
# setup(
#     name = "PyDracula",
#     version = "1.0",
#     description = "Modern GUI for Python applications",
#     author = "Wanderson M. Pimenta",
#     options = {'build_exe' : {'include_files' : files,
#                               'build_exe': build_folder,
#                               'excludes': excludes,
#                               'packages': packages,
#                               'optimize': 2,
#                               }
#                 },
#     executables = [target])