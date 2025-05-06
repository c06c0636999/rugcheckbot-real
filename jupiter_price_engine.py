import requests

def get_token_fdv(token_address):
    try:
        url = f"https://price.jup.ag/v4/token/{token_address}"
        response = requests.get(url)
        if response.status_code != 200:
            print("Jupiter 查價失敗")
            return None

        data = response.json()
        fdv = data.get("fdv", None)
        if fdv:
            return f"${round(fdv):,}"
        return None
    except Exception as e:
        print("查詢 FDV 發生錯誤：", e)
        return None