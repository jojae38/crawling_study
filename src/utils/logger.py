import logging
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.config.path_manager import LOG_DIR


# 로그 파일 저장 위치 설정

LOG_DIR.mkdir(exist_ok=True)  # logs 디렉터리가 없으면 생성

# 로그 설정
logging.basicConfig(
    filename=LOG_DIR / 'app.log',  # 로그 파일 위치
    level=logging.ERROR,           # ERROR 레벨 이상만 기록
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_error(message):
    logging.error(message)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

log_error("이 로그는 에러 메시지로 기록됩니다.")
log_info("이 로그는 정보 메시지로 기록됩니다.") 
log_warning("이 로그는 경고 메시지로 기록됩니다.")

print("로그 파일을 열어보세요.")