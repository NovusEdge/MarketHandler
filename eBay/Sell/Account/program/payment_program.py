import requests

def get_payment_program(marketplace_id: str, program_type: str, onboarding=False):
    if onboarding:
        r = requests.get(f"https://api.sandbox.ebay.com/sell/account/v1/payment_program/{marketplace_id}/{program_type}/onboarding")

    r = requests.get(f"https://api.sandbox.ebay.com/sell/account/v1/payment_program/{marketplace_id}/{program_type}")
    return r
