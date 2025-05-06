import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_alert(token, info):
    token_str = f"{token['name']} 合約: {token['address']}"
    msg = f"金狗幣偵測！\n{token_str}\n爆發分數：{info['爆發分數']}\nFDV：{info['FDV']}\nRug風險：{info['Rug風險']}"
    url = f"https://api.telegram.org/bot{os.getenv('TG_BOT_TOKEN')}/sendMessage"
    requests.post(url, json={"chat_id": os.getenv("TG_CHAT_ID"), "text": msg})
