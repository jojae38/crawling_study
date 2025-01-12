from pathlib import Path
import sys

# 0. 가상환경 설정 ()

# 1. 경로 설정
PROJECT_ROOT = Path(__file__).resolve().parent

SRC_ROOT = PROJECT_ROOT / 'src'
LOG_ROOT = SRC_ROOT / 'logs'
ASSET_ROOT = SRC_ROOT / 'assets'

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

