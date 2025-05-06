import requests
import os

def get_new_tokens():
    url = "https://mainnet.helius-rpc.com/?api-key=" + os.getenv("HELIUS_API_KEY")
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "id": "scan-tokens",
        "method": "getAssetsByGroup",
        "params": {
            "groupKey": "collection",
            "groupValue": "mint",
            "page": 1,
            "limit": 5
        }
    }

    try:
        res = requests.post(url, json=payload, headers=headers)
        data = res.json()
        tokens = []

        for item in data.get("result", {}).get("items", []):
            token_info = {
                "name": item.get("content", {}).get("metadata", {}).get("name", "Unknown"),
                "address": item.get("id", ""),
            }
            tokens.append(token_info)

        return tokens

    except Exception as e:
        print("抓取鏈上新幣失敗：", e)
        return []
