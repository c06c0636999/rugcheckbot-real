import time
from solana_scanner import get_new_tokens
from rugcheck_engine import is_token_safe
from potential_moon_shot_engine import evaluate_token_potential
from telegram_bot import send_alert

SCAN_INTERVAL = 180  # 每三分鐘掃描一次

def main_loop():
    print("RugCheckBot 已啟動，開始掃描...")
    seen_tokens = set()

    while True:
        try:
            print("\n--- 新一輪掃描開始 ---")
            new_tokens = get_new_tokens()
            print(f"共發現 {len(new_tokens)} 個交易池")

            for token in new_tokens:
                if token['address'] not in seen_tokens:
                    print(f"發現新幣：{token['name']} ({token['address']})")
                    seen_tokens.add(token['address'])

                    if is_token_safe(token['address']):
                        print(f"{token['name']} 通過 rug 檢查，進行潛力評估中...")
                        potential_info = evaluate_token_potential(token)
                        send_alert(token, potential_info)
                    else:
                        print(f"{token['name']} 未通過 rug 檢查，已略過")

        except Exception as e:
            print("錯誤發生：", e)

        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main_loop()
