from pathlib import Path
import datetime
from utils.logger import *

class ErrorCode:
    UNKNOWN_ERROR = 'E0000'
    FILE_NOT_FOUND = 'E0001'
    INVALID_INPUT = 'E0002'
    PERMISSION_DENIED = 'E0003'
    DATABASE_ERROR = 'E0004'
    NETWORK_ERROR = 'E0005'
    AUTHENTICATION_FAILED = 'E0006'


ERROR_MESSAGES = {
    ErrorCode.UNKNOWN_ERROR: "알 수 없는 오류가 발생했습니다.",
    ErrorCode.FILE_NOT_FOUND: "파일을 찾을 수 없습니다.",
    ErrorCode.INVALID_INPUT: "잘못된 입력입니다.",
    ErrorCode.PERMISSION_DENIED: "권한이 부족합니다.",
    ErrorCode.DATABASE_ERROR: "데이터베이스 오류가 발생했습니다.",
    ErrorCode.NETWORK_ERROR: "네트워크 연결에 실패했습니다.",
    ErrorCode.AUTHENTICATION_FAILED: "인증에 실패했습니다."
}


def get_error_message(error_code: str) -> str:
    return ERROR_MESSAGES.get(error_code, ERROR_MESSAGES[ErrorCode.UNKNOWN_ERROR])


class CustomError(Exception):
    def __init__(self, error_code, action=None):
        self.error_code = error_code
        self.message = get_error_message(error_code)
        self.action = action
        super().__init__(self.message)

        # 로그 기록
        log_error(f"[{self.error_code}] {self.message}")
        
        # 후처리 작업 실행
        if self.action:
            self.handle_action()

    def handle_action(self):
        if callable(self.action):
            self.action()
        else:
            print(f"후처리 작업이 정의되지 않았습니다: {self.error_code}")
