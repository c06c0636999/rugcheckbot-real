import requests

def is_token_safe(address):
    # 模擬檢查邏輯，可替換為真實風控 API
    return address is not None and len(address) > 20
