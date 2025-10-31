from PIL import Image
import os

# 圖片資料夾路徑
IMAGE_DIR = "IMAGE"

def load_background():
    """載入底圖 X1.JPG"""
    bg_path = os.path.join(IMAGE_DIR, "JERRY.JPG")
    return Image.open(bg_path)

def load_symbol_images():
    """載入 S01~S09.jpg 圖案"""
    symbol_images = {}
    for i in range(1, 10):
        filename = f"S0{i}.jpg"
        path = os.path.join(IMAGE_DIR, filename)
        symbol_images[filename] = Image.open(path)
    return symbol_images