import time
from solana_scanner import get_new_tokens
from rugcheck_engine import is_token_safe
from potential_moon_shot_engine import evaluate_token_potential
from telegram_bot import send_alert

def main_loop():
    print("啟動 RugCheckBot 實戰版")
    scanned = set()
    while True:
        try:
            tokens = get_new_tokens()
            for token in tokens:
                if token['address'] in scanned:
                    continue
                scanned.add(token['address'])

                if is_token_safe(token['address']):
                    info = evaluate_token_potential(token)
                    send_alert(token, info)
        except Exception as e:
            print("錯誤：", e)
        time.sleep(180)

if __name__ == "__main__":
    main_loop()