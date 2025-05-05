import requests
import os

def get_new_tokens():
    headers = { "Authorization": f"Bearer {os.getenv('HELIUS_API_KEY')}" }
    url = "https://api.helius.xyz/v0/tokens/most-recent?limit=10"
    response = requests.get(url, headers=headers)
    data = response.json()
    tokens = []
    for item in data:
        tokens.append({
            "name": item.get("tokenInfo", {}).get("name", "Unknown"),
            "address": item.get("tokenAddress")
        })
    return tokens
