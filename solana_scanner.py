import requests
import os

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

def get_new_tokens():
    url = f"https://api.helius.xyz/v0/tokens/most-recent?api-key={HELIUS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        print("獲取新幣失敗:", response.text)
        return []

    tokens = []
    data = response.json()
    for item in data:
        token_info = {
            "name": item.get("name", ""),
            "address": item.get("mint", ""),
            "symbol": item.get("symbol", ""),
            "decimals": item.get("decimals", 0)
        }
        tokens.append(token_info)

    return tokens
