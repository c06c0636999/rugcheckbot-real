import requests
import os

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

def is_token_safe(token_address):
    url = f"https://api.helius.xyz/v0/tokens/{token_address}/metadata?api-key={HELIUS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        print("無法取得 rug 資訊:", response.text)
        return False

    data = response.json()
    if not data.get("isLiquidityLocked", True):
        return False
    if data.get("buyTax", 0) > 10 or data.get("sellTax", 0) > 10:
        return False
    if data.get("hasBlacklist", False) or data.get("hasMintAuthority", False):
        return False

    return True