import time
from solana_scanner import get_new_tokens
from rugcheck_engine import is_token_safe
from potential_moon_shot_engine import evaluate_token_potential
from telegram_bot import send_alert

SCAN_INTERVAL = 180  # 每 3 分鐘掃一次

def main_loop():
    print("✅ RugCheckBot 已啟動，開始掃描鏈上新幣...")
    seen_tokens = set()

    while True:
        try:
            new_tokens = get_new_tokens()
            print("🔍 抓到新幣：", new_tokens)

            for token in new_tokens:
                if token['address'] not in seen_tokens:
                    print(f"➡️ 檢查新幣: {token['name']} ({token['address']})")
                    seen_tokens.add(token['address'])

                    if is_token_safe(token['address']):
                        potential_info = evaluate_token_potential(token)
                        send_alert(token, potential_info)

        except Exception as e:
            print("⚠️ 錯誤：", e)

        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main_loop()
