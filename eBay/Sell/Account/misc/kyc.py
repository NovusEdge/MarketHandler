import requests

def get_kyc():
    r = requests.get("https://api.ebay.com/sell/account/v1/kyc")
    return r
