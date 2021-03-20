import urllib3
import os, sys, subprocess
import json, pickle
from policy import fulfill, payment, return_pol
from program import payment_program, programs
from misc import kyc, privilige, rates, sales_tax

class Account(object):
    # TODO: Complete the docs for this....
    '''

    '''

    def __init__(self):
        with open("../../.mainconfig/config.dat", "r") as f:
            config = pickle.load(f)

            if not any(config):
                raise Exception("Run setup.py first")

            self.username = config["username"]
            self.app_id   = config["app_id"]
            self.dev_id   = config["dev_id"]
            self.secret   = config["client_secret"]
