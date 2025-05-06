import time
from solana_scanner import get_new_tokens
from telegram_bot import send_alert

SCAN_INTERVAL = 180  # 每 3 分鐘掃一次

def main_loop():
    print("RugCheckBot 已啟動...")
    seen_tokens = set()
    while True:
        try:
            new_tokens = get_new_tokens()
            print("掃描結果：", new_tokens)

            for token in new_tokens:
                if token["address"] not in seen_tokens:
                    print(f"新幣發現: {token['name']} ({token['address']})")
                    seen_tokens.add(token["address"])

                    # 模擬爆發分數，後續可替換為 evaluate_token_potential
                    fake_info = {"爆發分數": 88, "FDV": "$20K", "Rug風險": "低"}
                    send_alert(token, fake_info)

        except Exception as e:
            print("錯誤:", e)
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main_loop()
