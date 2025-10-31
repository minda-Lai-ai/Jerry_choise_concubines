# 遊戲設定
SYMBOL_FILES = [f"S0{i}.jpg" for i in range(1, 10)]
SYMBOL_WEIGHTS = {f"S0{i}.jpg": 1 for i in range(1, 10)}  # 可調整機率
BACKGROUND_PATH = "assets/background/X1.JPG"
SYMBOL_PATH = "assets/symbols/"
SLOT_SIZE_RATIO = 0.3
SLOT_POSITION = {"bottom": 0.1, "right": 0.1}