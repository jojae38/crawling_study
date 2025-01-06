#!/bin/bash

# 1. 가상환경 설치
echo "🐍 가상환경 설치 중..."
python -m venv venv
source venv/bin/activate

# 2. 개발에 필요한 패키지 설치
echo "🔧 개발에 필요한 패키지 설치 중..."
pip install -r dev_requirements.txt

