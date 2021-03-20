import requests

def create_replace_sales_tax(country_code: str, jurisdiction_id: str, payload: dict):
    r = requests.put(f"https://api.sandbox.ebay.com/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}", data=payload)
    return r


def delete_sales_tax(country_code: str, jurisdiction_id: str):
    r = requests.delete(f"https://api.sandbox.ebay.com/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")
    return r

def get_sales_tax(country_code: str, jurisdiction_id: str):
    r = requests.get(f"https://api.sandbox.ebay.com/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")
    return r

def get_sales_taxes():
    r = requests.get(f"https://api.sandbox.ebay.com/sell/account/v1/sales_tax")
    return r
