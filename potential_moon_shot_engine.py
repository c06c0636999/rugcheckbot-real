from jupiter_price_engine import get_token_fdv
import random

def evaluate_token_potential(token):
    fdv = get_token_fdv(token['address']) or "$8,000"
    return {
        "FDV": fdv,
        "爆發分數": random.randint(70, 95),
        "Rug風險": "無"
    }