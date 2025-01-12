import subprocess
import sys
import importlib.metadata

def install_requirements():
    """
    requirements.txt 내부 라이브러리 설치
    """
    try:
        # requirements.txt 파일 읽기
        with open('requirements.txt', 'r') as file:
            requirements = file.read().splitlines()
        
        # 설치되어 있는 패키지 확인
        installed_packages = {pkg.metadata['Name'].lower() for pkg in importlib.metadata.distributions()}
        
        # 필요한 패키지 설치
        for package in requirements:
            pkg_name = package.split('==')[0]  # 버전 제거하고 패키지 이름만 추출
            if pkg_name.lower() not in installed_packages:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                
        print("All requirements are installed.")
    
    except Exception as e:
        print(f"Failed to install packages: {e}")


def uninstall_requirements():
    """
    requirements.txt 내부 라이브러리 삭제
    """
    try:
        # requirements.txt 파일 읽기
        with open('requirements.txt', 'r') as file:
            requirements = file.read().splitlines()
        
        # requirements.txt에 있는 모든 패키지 삭제
        for package in requirements:
            pkg_name = package.split('==')[0]  # 버전 제거하고 패키지 이름만 추출
            print(f"Uninstalling {pkg_name}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', pkg_name])
        
        print("All listed packages have been uninstalled.")

    except Exception as e:
        print(f"Failed to uninstall packages: {e}")
