import requests

def get_opted_in_programs():
    r = requests.get("https://api.sandbox.ebay.com/sell/account/v1/program/get_opted_in_programs")
    return r

def opt_into_program(payload: dict):
    r = requests.post("https://api.sandbox.ebay.com/sell/account/v1/program/opt_in", data=payload)
    return r

def opt_out_of_program(payload: dict):
    r = requests.post("https://api.sandbox.ebay.com/sell/account/v1/program/opt_out", data=payload)
