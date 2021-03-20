import requests

def get_privileges():
    r = requests.get("https://api.sandbox.ebay.com/sell/account/v1/privilege")
    return r
