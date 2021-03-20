import requests


def create_payment_policy(payload: dict):
    r = requests.post("https://api.sandbox.ebay.com/sell/account/v1/payment_policy", data=payload)
    return r

def delete_payment_policy(policy_id: str):
    r = requests.delete(f"https://api.sandbox.ebay.com/sell/account/v1/payment_policy/{policy_id}")
    return r

def get_payment_policies(marketplace_id: str):
    r = requests.get("https://api.sandbox.ebay.com/sell/account/v1/payment_policy?marketplace_id={marketplace_id}")
    return r

def get_payment_policy(policy_id: str, marketplace_id: str, name: str, policy_name=None):

    if policy_name not None:
        r_name = requests.get(f"https://api.sandbox.ebay.com/sell/account/v1/payment_policy/get_by_policy_name?name={name}&marketplace_id={marketplace_id}")
    else:
        r_name = None

    r_pol = requests.get(f"https://api.sandbox.ebay.com/sell/account/v1/payment_policy/{policy_id}")
    return r_pol, r_name

def update_payment_policy(policy_id: str, payload: dict):
    r = requests.put(f"https://api.sandbox.ebay.com/sell/account/v1/payment_policy/{policy_id}", data=payload)
    return r
