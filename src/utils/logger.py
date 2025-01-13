import logging
from logging.handlers import TimedRotatingFileHandler
from utils.directories import DIRS_DICT

LOG_LEVEL = logging.DEBUG
LOG_BACKUP_COUNT = 7  # 로그 파일 백업 개수

# 로거 설정
logger = logging.getLogger('DailyLog')
logger.setLevel(LOG_LEVEL)

# 날짜별 로그 파일 핸들러 설정
file_handler = TimedRotatingFileHandler(
    filename=DIRS_DICT['LOG_DIR'] / "daily_log.log", 
    when="midnight", 
    interval=1, 
    encoding="utf-8", 
    backupCount=LOG_BACKUP_COUNT
)

# 파일명에 날짜 추가
file_handler.suffix = '%Y%m%d.log' 
log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(log_formatter)

# 파일명에 날짜 형식 추가
# file_handler.namer = lambda name: f"{name}.log"

# 콘솔 핸들러 추가
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

# 핸들러를 로거에 추가
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_error(message):
    logger.error(message)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

log_error("이 로그는 에러 메시지로 기록됩니다.")
log_info("이 로그는 정보 메시지로 기록됩니다.") 
log_warning("이 로그는 경고 메시지로 기록됩니다.")

print("로그 파일을 열어보세요.")