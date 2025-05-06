import time
from solana_scanner import get_new_tokens
from rugcheck_engine import is_token_safe
from potential_moon_shot_engine import evaluate_token_potential
from telegram_bot import send_alert

SCAN_INTERVAL = 180  # 每 3 分鐘掃描一次

def main_loop():
    print("RugCheckBot 已啟動...")
    seen_tokens = set()

    while True:
        try:
            print("\n--- 新一輪掃描開始 ---")
            new_tokens = get_new_tokens()
            print(f"發現 {len(new_tokens)} 筆代幣")

            for token in new_tokens:
                if token['address'] not in seen_tokens:
                    print(f"\n[新幣發現] 名稱：{token['name']}，地址：{token['address']}")
                    seen_tokens.add(token['address'])

                    if is_token_safe(token['address']):
                        print("→ 通過 rugcheck 檢查，進行爆發潛力分析...")
                        potential_info = evaluate_token_potential(token)
                        print(f"→ 分析結果：FDV={potential_info['FDV']}，風險={potential_info['Rug風險']}")
                        send_alert(token, potential_info)
                        print("→ 已送出 Telegram 推播")
                    else:
                        print("→ 未通過 rug 檢查，略過")
                else:
                    print(f"[跳過重複] {token['name']} ({token['address']})")

        except Exception as e:
            print("⚠️ 發生錯誤：", e)

        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main_loop()
