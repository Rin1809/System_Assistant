# utils/cau_hinh.py
import threading
import sys
import codecs
import os
import re
# Khóa Rin
PRINT_LOCK = threading.Lock()

# Màu sắc
PINK1 = "\033[38;2;255;192;203m"
PLUM2 = "\033[38;2;221;160;221m"
RICH_PINK = "\033[38;2;255;105;180m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[38;5;226m"  # Nền vàng nhạt
BLUE = "\033[94m"
ORANGE = "\033[38;2;255;105;180m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNBOLD = "\033[0m"
GREEN = "\033[38;5;154m"
RIN = "\033[38;5;159m"
TIME = "\033[38;5;231m"
THISTLE1 = "\033[38;2;255;225;255m"
DARK_ORANGE = "\033[38;2;255;140;0m"
MODEL_NAME = "gemini-2.0-flash" # Thay doi model neu can
MODEL_NAME2 = "gemini-exp-1206"
TEMP = 0.7
TOP_P = 0.95
TOP_K = 40
MAX_OUTPUT_TOKENS = 8192 #giam xuon == nhanh hon
API_KEY = "AIzaSyCFmeHgOho-pX0sFfBoGYEuP0FEMHuBoWc"

SUCCESS = f"{GREEN}✔{RESET}"
FAIL = f"{RED}❌{RESET}"
ERROR = f"{RED}⚠{RESET}"

# path luu memory
MEMORY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "memory")

MEMORY_FILE_FORMAT = "Memory_%Y-%m-%d_%H-%M-%S.json"
SESSION_FILE_FORMAT = "Session_%Y-%m-%d_%H-%M-%S.json"

def remove_ansi_escape_codes(text):
    """Loại bỏ mã màu ANSI khỏi chuỗi."""
    return re.sub(r'\x1b\[[0-9;]*[mG]', '', text)