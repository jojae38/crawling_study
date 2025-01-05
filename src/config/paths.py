from pathlib import Path

# 프로젝트 루트 및 assets 폴더 설정
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / 'assets'

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
FOLDERS = build_folder_structure(ASSETS_DIR)

def get_file_path(subdir: str, filename: str) -> Path:
    """자동 매핑된 폴더에서 파일 경로 반환"""
    if subdir in FOLDERS:
        target_path = FOLDERS[subdir] / filename
        if target_path.exists():
            return target_path
        else:
            print(f"{filename} 파일이 {target_path}에 없습니다.")
            return False
    else:
        print(f"{subdir} 서브 폴더가 존재하지 않습니다.")
        return False

# 사용 예시

# image_path = get_file_path('images/20141010', '1010.png')

