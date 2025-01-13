from pathlib import Path
import sys
import os
import shutil

# 0. 가상환경 설정 ()



# 1. 경로 설정
PROJECT_ROOT = Path(__file__).resolve().parent

# 2. 시스템 경로 설정 추가

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

SRC_ROOT = PROJECT_ROOT / 'src'
LOG_ROOT = SRC_ROOT / 'logs'
ASSET_ROOT = SRC_ROOT / 'assets'



def create_sitecustomize_file(project_path):
    # 프로젝트 경로 내에서 sitecustomize.py 생성
    sitecustomize_path = os.path.join(project_path, "sitecustomize.py")

    # sitecustomize.py 내용 작성
    content = """import sys\nimport os\n\n# 프로젝트 루트 경로를 계산\nproject_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))\nif project_root not in sys.path:\n    sys.path.insert(0, project_root)\n"""

    try:
        with open(sitecustomize_path, "w") as f:
            f.write(content)
        print(f"프로젝트 경로에 sitecustomize.py 파일이 생성되었습니다: {sitecustomize_path}")
    except Exception as e:
        print(f"Error: sitecustomize.py 파일 생성 중 문제가 발생했습니다: {e}")
        return None

    return sitecustomize_path

def copy_to_venv(venv_path, project_sitecustomize_path):
    # 가상환경 내 site-packages 경로 확인
    if os.name == "nt":
        site_packages_path = os.path.join(venv_path, "Lib", "site-packages")
    else:
        python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
        site_packages_path = os.path.join(venv_path, "lib", python_version, "site-packages")

    if not os.path.exists(site_packages_path):
        print(f"Error: site-packages 경로를 찾을 수 없습니다: {site_packages_path}")
        return

    # 파일 복사
    try:
        shutil.copy(project_sitecustomize_path, site_packages_path)
        print(f"sitecustomize.py 파일이 가상환경에 복사되었습니다: {site_packages_path}")
    except Exception as e:
        print(f"Error: 파일 복사 중 문제가 발생했습니다: {e}")
