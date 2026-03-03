import json
import os

SHOP_FILE = "shopping.json"

def load_list():
    if not os.path.exists(SHOP_FILE):
        return []
    with open(SHOP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    with open(SHOP_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
import os
import json

def ensure_prices_file():
    file_path = "src/shopping_list/prices.json"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4)
