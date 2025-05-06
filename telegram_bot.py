import requests
import os

def send_alert(token, info):
    token_str = f"{token['name']}｜合約: {token['address']}"
    msg = f"金狗潛力幣警報：\n{token_str}\nFDV：{info['FDV']}\nRug風險：{info['Rug風險']}"
    url = f"https://api.telegram.org/bot{os.getenv('TG_BOT_TOKEN')}/sendMessage"
    payload = {
        "chat_id": os.getenv("TG_CHAT_ID"),
        "text": msg
    }

    try:
        response = requests.post(url, json=payload)
        print(f"推播狀態碼: {response.status_code}")
        print(f"推播內容: {msg}")
        if not response.ok:
            print(f"推播錯誤訊息: {response.text}")
    except Exception as e:
        print(f"推播例外錯誤: {e}")
