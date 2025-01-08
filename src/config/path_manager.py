from pathlib import Path

# 전역
PROJECT_ROOT = ''
ASSETS_DIR = ''
LOG_DIR = ''

def path_manager_init():
    # 프로젝트 루트 및 assets 폴더 설정

    global PROJECT_ROOT, ASSETS_DIR

    PROJECT_ROOT = find_project_root('.git')
    ASSETS_DIR = PROJECT_ROOT / 'assets'
    LOG_DIR = PROJECT_ROOT / 'logs'

def find_project_root(target_file: str = '.git') -> Path:

    # 현재 파일이 실행되는 위치 기준
    current_path = Path(__file__).resolve()
    
    # 상위 디렉터리를 탐색
    for parent in current_path.parents:
        if (parent / target_file).exists():
            return parent
    
    # 파일을 찾지 못한 경우 예외 발생
    print(f"'{target_file}'을 포함하는 프로젝트 루트를 찾을 수 없습니다.")
    return 0

def build_folder_structure(base_dir: Path) -> dict:
    """assets 폴더 구조를 재귀적으로 탐색해 딕셔너리로 변환"""
    folder_dict = {}

    # assets 하위 폴더 및 파일 탐색
    for path in base_dir.rglob('*'):
        if path.is_dir():
            # 폴더일 경우 재귀적으로 탐색
            relative_path = path.relative_to(base_dir)
            folder_dict[str(relative_path)] = path
        elif path.is_file():
            # 파일일 경우 해당 경로를 폴더 딕셔너리에 추가
            relative_path = path.parent.relative_to(base_dir)
            folder_dict.setdefault(str(relative_path), path.parent)
    
    return folder_dict

# assets 폴더 구조를 딕셔너리로 매핑
def get_file_path(subdir: str, filename: str, folder_dic: dict) -> Path:
    """자동 매핑된 폴더에서 파일 경로 반환"""
    if subdir in folder_dic:
        target_path = folder_dic[subdir] / filename
        if target_path.exists():
            return target_path
        else:
            print(f"{filename} 파일이 {target_path}에 없습니다.")
            return False
    else:
        print(f"{subdir} 서브 폴더가 존재하지 않습니다.")
        return False


path_manager_init()

print(PROJECT_ROOT)
print(ASSETS_DIR)
# 프로젝트 루트 및 assets 폴더 설정
# PROJECT_ROOT = find_project_root('.git')
# ASSETS_DIR = PROJECT_ROOT / 'assets'
# FOLDERS = build_folder_structure(ASSETS_DIR)
# 사용 예시

# image_path = get_file_path('images/20141010', '1010.png')

