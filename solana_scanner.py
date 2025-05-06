import requests
import os

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

def get_new_tokens():
    url = f"https://api.helius.xyz/v0/addresses/activity?api-key={HELIUS_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "address": "HZoTGt1LtYDQKBPwYbnRvX3kJJNq8yp1KoVxZiK5YWEp",  # Jupiter DEX router
        "types": ["TOKEN_MINT"],
        "limit": 20
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print("獲取新幣活動失敗:", response.text)
        return []

    seen = set()
    tokens = []
    for item in response.json():
        mint = item.get("events", {}).get("mint", {}).get("mint")
        if mint and mint not in seen:
            seen.add(mint)
            tokens.append({
                "name": "NewToken",
                "address": mint
            })

    return tokens
