import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_alert(token, info):
    msg = f"潛力幣自動推播：金狗狙擊系統\n\n名稱： ${token['name']}\nMint： {token['address']}\n市值： {info['FDV']}\n爆發分數： {info['爆發分數']}\nRug 安全檢查：\n→ 狀態：{info['Rug風險']}\n\n#RugCheckBot #金狗幣"
    url = f"https://api.telegram.org/bot{os.getenv('TG_BOT_TOKEN')}/sendMessage"
    requests.post(url, json={"chat_id": os.getenv("TG_CHAT_ID"), "text": msg})