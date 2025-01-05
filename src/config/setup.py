import subprocess
from pathlib import Path
import shutil
import os

def build_exe():
    separator = ";" if os.name == 'nt' else ":"
    
    pyinstaller_cmd = [
        "pyinstaller",
        "--onefile",
        "--name", "main",
        "--add-data", f"assets{separator}assets",
        "main.py"
    ]
    
    result = subprocess.run(pyinstaller_cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("PyInstaller 빌드 성공")
        copy_to_release()
    else:
        print("PyInstaller 빌드 실패")
        print(result.stderr)

def copy_to_release():
    dist_exe = Path("dist/main.exe")
    release_dir = Path("../release")
    release_assets = release_dir / "assets"
    src_assets = Path("assets")

    release_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(dist_exe, release_dir / "main.exe")
    
    if src_assets.exists():
        if release_assets.exists():
            shutil.rmtree(release_assets)
        shutil.copytree(src_assets, release_assets)
    
    print("실행 파일 및 assets 폴더가 release 폴더에 복사되었습니다.")

if __name__ == "__main__":
    build_exe()
