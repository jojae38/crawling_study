from pathlib import Path

def create_folder(folder_path):
    """
    지정된 경로에 폴더가 없으면 폴더를 생성합니다.

    Args:
        folder_path (str or Path): 생성할 폴더의 경로.
    """
    folder_path = Path(folder_path)

    # 폴더가 없으면 생성
    if not folder_path.exists():
        folder_path.mkdir(parents=True)  # 부모 디렉토리까지 포함해서 생성
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
