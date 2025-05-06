import requests
import os

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

def get_new_tokens():
    url = f"https://api.helius.xyz/v0/addresses?api-key={HELIUS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        print("獲取新幣失敗:", response.text)
        return []

    data = response.json()
    tokens = []
    for item in data:
        if item.get("token", {}).get("is_native"):
            continue
        token_info = {
            "name": item["token"]["name"],
            "address": item["token"]["mint"],
            "symbol": item["token"].get("symbol", ""),
            "decimals": item["token"].get("decimals", 0)
        }
        tokens.append(token_info)

    return tokens