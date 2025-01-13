from setuptools import setup, find_packages

# requirements.txt에서 의존성 읽기
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

# 설치 정보 작성 
# pip install -e .
setup(
    name="utils_package",
    version="1.0.0",
    description="A reusable utilities package",
    author="jonus",
    url="https://github.com/jojae38/crawling_study",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
)
