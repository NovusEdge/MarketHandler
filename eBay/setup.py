import sys, os
import pathlib
import argparse
import pickle

# --------- arg_status --------- :
username_ok = False
app_id_ok   = False
dev_id_ok   = False
cert_id_ok  = False
# ------------------------------

parser = argparse.ArgumentParser()
PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

# ------------------------------- Arguments ------------------------------------
parser.add_argument('-username', '--set-username',
                    type=str,
                    help='<username>    set the username to [username]'
)
parser.add_argument('-app_id', '--set-app_id',
                    type=str,
                    help='<id>    sets the App ID (Client ID) to [app_id]'
)
parser.add_argument('-dev_id', '--set-dev_id',
                    type=str,
                    help='<dev_id>    sets the Dev Id to [dev_id]'
)
parser.add_argument('-cert', '--set-client_secret', '--set-cert_id',
                    type=str,
                    help='<client_secret>    sets the Client secret to \
                    [client_secret]'
)
# ------------------------------------------------------------------------------


args = parser.parse_args()

# ----------- Checking for arg status ------------
if args.set_username:
    username_ok = True

if args.set_app_id:
    app_id_ok = True

if args.set_dev_id:
    dev_id_ok = True

if args.set_client_secret:
    cert_id_ok = True
# -------------------------------------------------

if __name__ == "__main__":
    conf = open(".mainconfig/config.dat", "wb")

    pickle.dump({
        "username": args.set_username,
        "app_id": args.set_app_id,
        "dev_id": args.set_dev_id,
        "client_secret": args.set_client_secret
    }, conf)

    conf.close()

'''
python3 setup.py -username=fermi \
-app_id=AlexPrio-ShopMini-SBX-4dc6ffda4-36ac3745 \
-dev_id=4202d90a-c4db-4a9e-aa8e-27e2cfc72d72 \
-cert=SBX-dc6ffda47286-fef1-456e-9e31-38af
'''
