#!/bin/bash

# 1. 배포 시작 메시지
echo "🚀 배포 시작..."

# 2. 환경 설정
APP_NAME="my_app"
BUILD_DIR="release"
SERVER_USER="user"
SERVER_IP="192.168.1.10"
DEPLOY_PATH="/var/www/$APP_NAME"

# 3. 프로젝트 빌드
echo "🔧 프로젝트 빌드 중..."
python setup.py build

# 4. 압축 및 패키징
echo "📦 파일 압축 중..."
zip -r $BUILD_DIR/app.zip src/ requirements.txt

# 5. 서버로 전송
echo "📤 서버에 전송 중..."
scp $BUILD_DIR/app.zip $SERVER_USER@$SERVER_IP:$DEPLOY_PATH

# 6. 서버에서 애플리케이션 재시작
echo "🔄 서버 재시작 중..."
ssh $SERVER_USER@$SERVER_IP << 'EOF'
    cd /var/www/my_app
    unzip -o app.zip
    sudo systemctl restart my_app
EOF

# 7. 상태 확인
echo "✅ 배포 완료! 애플리케이션 상태 확인 중..."
ssh $SERVER_USER@$SERVER_IP "curl http://localhost:5000/health-check"

echo "🎉 배포가 완료되었습니다!"
