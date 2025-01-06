import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# VERSION
version = "1.0"
build_folder = f"release/{version}"

# EXCLUDES
excludes = ['tkinter']

# INCLUDE PACKAGES - 다른 환경에서 실행시키려면 필요함
packages = ['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico",
    target_name="PyDracula.exe",
)

# SETUP CX FREEZE
setup(
    name = "PyDracula",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "Wanderson M. Pimenta",
    options = {'build_exe' : {'include_files' : files,
                              'build_exe': build_folder,
                              'excludes': excludes,
                              'packages': packages,
                              'optimize': 2,
                              }
                },
    executables = [target]
)
