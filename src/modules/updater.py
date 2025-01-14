# 업데이트 기능

import requests
import zipfile
import shutil
from pathlib import Path
import subprocess
import os

# GitHub 정보
GITHUB_REPO = "username/repository"
CURRENT_VERSION = "1.0.0"
RELEASE_DIR = Path(__file__).resolve().parent / '../release'

def get_latest_release():
    """GitHub Release API에서 최신 릴리즈 정보 가져오기"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        release_data = response.json()
        return release_data['tag_name'], release_data['assets']
    else:
        raise Exception("최신 릴리즈 정보를 가져오지 못했습니다.")

def download_asset(asset_url, output_path):
    """Release에서 파일 다운로드"""
    response = requests.get(asset_url, stream=True)
    with open(output_path, 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    print(f"{output_path.name} 다운로드 완료.")

def update_application():
    try:
        latest_version, assets = get_latest_release()

        if latest_version == CURRENT_VERSION:
            print("현재 최신 버전입니다.")
            return
        
        print(f"새 버전 발견: {latest_version}. 업데이트를 진행합니다.")
        
        # 임시 폴더 생성
        temp_dir = Path("temp_update")
        temp_dir.mkdir(exist_ok=True)

        # assets에서 main.exe 및 assets.zip 다운로드
        for asset in assets:
            asset_name = asset['name']
            asset_url = asset['browser_download_url']
            
            # exe 및 assets.zip 다운로드
            if asset_name.endswith('.exe') or asset_name.endswith('.zip'):
                download_asset(asset_url, temp_dir / asset_name)
        
        # 파일 덮어쓰기
        for file in temp_dir.glob('*'):
            if file.suffix == '.exe':
                shutil.move(file, RELEASE_DIR / 'main.exe')
            elif file.suffix == '.zip':
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(RELEASE_DIR / 'assets')
        
        print("업데이트 완료. 프로그램을 재시작합니다.")
        
        # 프로그램 재시작
        subprocess.Popen([str(RELEASE_DIR / 'main.exe')])
        os._exit(0)

    except Exception as e:
        print(f"업데이트 중 오류 발생: {e}")

if __name__ == "__main__":
    update_application()
