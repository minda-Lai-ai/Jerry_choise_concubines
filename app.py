import streamlit as st
from PIL import Image
import os
import random
import time
import base64

# --- 設定 ---
st.set_page_config(layout="wide")

# --- 圖片路徑 ---
IMAGE_DIR = "IMAGE"
BACKGROUND_FILE = "JERRY.JPG"
SYMBOL_FILES = [f"s0{i}.jpg" for i in range(1, 10)]

# 圖片的顯示寬度調整為 68 (原 90 * 0.75)
IMAGE_WIDTH = 68 
IMAGE_HEIGHT_CSS = f"{IMAGE_WIDTH}px" # 68px

# --- 載入圖片 ---
def load_image(filename):
    path = os.path.join(IMAGE_DIR, filename)
    try:
        return Image.open(path)
    except FileNotFoundError:
        st.error(f"檔案不存在：{path}")
        st.stop()
        
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"背景圖片檔案不存在：{image_path}")
        st.stop()

# --- 背景圖 base64 編碼 ---
background_path = os.path.join(IMAGE_DIR, BACKGROUND_FILE)
bg_base64 = get_base64_image(background_path)

# --- 載入轉輪圖 ---
symbol_images = {name: load_image(name) for name in SYMBOL_FILES}
symbol_weights = {
    "s01.jpg": 30,
    "s02.jpg": 20,
    "s03.jpg": 5,
    "s04.jpg": 5,
    "s05.jpg": 5,
    "s06.jpg": 5,
    "s07.jpg": 5,
    "s08.jpg": 10,
    "s09.jpg": 15
}

# --- 中獎機率設定 ---
JACKPOT_PROBABILITY = 0.3

# --- 特定中獎訊息設定 ---
JACKPOT_MESSAGES = {
    "s01.jpg": "🔥🔥🔥 恭喜邱貴妃奪冠，耀豊哥必然一瀉千里！ 🔥🔥🔥",
    "s02.jpg": "👑 皇上欽點GP桃木乃，耀豊哥一發中的！ 👑",
    "s03.jpg": "💎 飢渴的草人妃中獎，耀豊哥全力以赴！ 💎",
    "s04.jpg": "💰 捅痔成嬪，搞得耀豊哥大滿貫！ 💰",
    "s05.jpg": "🌈 完美，耀豊哥的最愛，精益求精！ 🌈",
    "s06.jpg": "🌟 看來昕經要吃醋了，不然約他一起！ 🌟",
    "s07.jpg": "🔱 心之所望，若不全力以赴怎對得起此群眾生！ 🔱",
    "s08.jpg": "💖 金色狂風！金色狂風！金色狂風！金色狂風！ 💖",
    "s09.jpg": "🎉 天下床術，唯肛不敗！精肛王要大展鴻圖了 🎉",
}


# --- 抽牌邏輯 ---
def spin_symbol():
    return random.choices(SYMBOL_FILES, weights=symbol_weights.values(), k=1)[0]

def evaluate_result(result):
    a, b, c = result
    if a == b == c:
        return JACKPOT_MESSAGES.get(a, f"🎉 中獎啦！{a} 三連發！")
    elif a == b or b == c or a == c:
        return "💖 耀豊哥要加油了，妃子們等不及了"
    else:
        return "😢 看來皇上今晚得自己來一發了~~~ T T"

# --- 背景與拉霸機 CSS ---
st.markdown(f"""
    <style>
    /* 全局背景 */
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    
    /* 右上角按鈕容器 */
    .pull-button-container {{
        position: fixed;
        top: 3%; 
        right: 3%; 
        z-index: 20; 
    }}

    /* 右下方拉霸機容器 */
    .slot-container {{
        position: fixed;
        bottom: 3%; 
        right: 3%; 
        width: 320px; 
        background-color: rgba(255, 255, 255, 0.85);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); 
        z-index: 10;
        text-align: center;
        display: flex; 
        flex-direction: column;
        justify-content: flex-end; 
        align-items: center; 
    }}

    /* 確保圖片所在的 Streamlit 內部容器高度固定 (解決往下掉問題) */
    /* st.columns 內部通常是使用 data-testid="stVerticalBlock" */
    .slot-container div[data-testid="stVerticalBlock"] > div:nth-child(2) {{
        min-height: {IMAGE_HEIGHT_CSS}; 
        height: {IMAGE_HEIGHT_CSS};
        display: flex; /* 確保內容居中或固定 */
        align-items: center;
        justify-content: center;
    }}
    
    /* 跑馬燈字體調整 (兩倍大) */
    .marquee {{
        font-size: 40px; 
        color: red;
        font-weight: bold;
        margin-bottom: 10px;
        height: 50px; 
        line-height: 50px; 
        overflow: hidden; 
    }}

    /* 圖片尺寸調整 (75%) 與固定高度 */
    .image-row img {{
        width: {IMAGE_HEIGHT_CSS} !important; 
        height: {IMAGE_HEIGHT_CSS} !important; 
        object-fit: contain; 
        border-radius: 5px;
        border: 2px solid #ccc; 
    }}
    
    /* 調整按鈕樣式 (維持不變) */
    .stButton > button {{
        background-color: #007bff; 
        color: white;
        padding: 15px 30px; 
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.2s ease;
    }}
    .stButton > button:hover {{
        background-color: #0056b3;
        transform: translateY(-2px);
    }}
    .stButton > button:active {{
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }}
    </style>
""", unsafe_allow_html=True)

# --- 拉桿按鈕 UI (右上角) ---
st.markdown('<div class="pull-button-container">', unsafe_allow_html=True)
pull_button = st.button("拉桿！", key="pull_lever_top_right")
st.markdown('</div>', unsafe_allow_html=True)


# --- 拉霸機 UI (右下方) ---
st.markdown('<div class="slot-container">', unsafe_allow_html=True)
st.markdown("<h3>🎰 拉霸機</h3>", unsafe_allow_html=True)

result_placeholder = st.empty() # 跑馬燈結果
# 使用 st.columns 來並排顯示圖片，並使用 placeholder 佔位
col1, col2, col3 = st.columns([1, 1, 1]) 

# 圖片的佔位符
reel1_placeholder = col1.empty()
reel2_placeholder = col2.empty()
reel3_placeholder = col3.empty()


# 初始化顯示狀態
if 'initial_spin' not in st.session_state:
    st.session_state.initial_spin = True
    # 初始時顯示隨機圖片
    reel1_placeholder.image(symbol_images[random.choice(SYMBOL_FILES)], width=IMAGE_WIDTH, use_column_width="always")
    reel2_placeholder.image(symbol_images[random.choice(SYMBOL_FILES)], width=IMAGE_WIDTH, use_column_width="always")
    reel3_placeholder.image(symbol_images[random.choice(SYMBOL_FILES)], width=IMAGE_WIDTH, use_column_width="always")
    # 跑馬燈速度調整為 12
    result_placeholder.markdown('<marquee class="marquee" scrollamount="12">點擊「拉桿！」開始遊戲</marquee>', unsafe_allow_html=True)

# 滾動與結果邏輯
if pull_button:
    st.session_state.initial_spin = False
    
    # 滾動動畫
    # 第一個滾輪
    for i in range(10):
        reel1_placeholder.image(symbol_images[random.choice(SYMBOL_FILES)], width=IMAGE_WIDTH, use_column_width="always")
        time.sleep(0.05)
    final1 = spin_symbol()
    reel1_placeholder.image(symbol_images[final1], width=IMAGE_WIDTH, use_column_width="always")

    # 第二個滾輪
    for i in range(10):
        reel2_placeholder.image(symbol_images[random.choice(SYMBOL_FILES)], width=IMAGE_WIDTH, use_column_width="always")
        time.sleep(0.05)
    final2 = spin_symbol()
    reel2_placeholder.image(symbol_images[final2], width=IMAGE_WIDTH, use_column_width="always")

    # 第三個滾輪
    for i in range(10):
        reel3_placeholder.image(symbol_images[random.choice(SYMBOL_FILES)], width=IMAGE_WIDTH, use_column_width="always")
        time.sleep(0.05)
    final3 = spin_symbol()
    reel3_placeholder.image(symbol_images[final3], width=IMAGE_WIDTH, use_column_width="always")

    result = [final1, final2, final3]
    message = evaluate_result(result)
    
    # 跑馬燈速度調整為 12
    result_placeholder.markdown(
        f'<marquee class="marquee" scrollamount="18">{message}</marquee>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)