import random
from config import SYMBOL_FILES, SYMBOL_WEIGHTS

def spin_symbol():
    return random.choices(SYMBOL_FILES, weights=SYMBOL_WEIGHTS.values(), k=1)[0]

def spin_reels():
    return [spin_symbol() for _ in range(3)]