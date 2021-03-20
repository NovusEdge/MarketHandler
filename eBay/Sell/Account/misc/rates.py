import requests

def get_rate_tables():
    r = requests.get("https://api.ebay.com/sell/account/v1/rate_table")
    return r
