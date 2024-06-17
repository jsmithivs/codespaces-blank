from sys import gettrace
import requests
from Connectwise.kv_secrets import get_secret

def is_debugging():
    return gettrace() is not None

public_key = get_secret("cw-public-key")
private_key = get_secret("cw-private-key")

username = f"training+{public_key}" if is_debugging() else f"iventure+{public_key}"
password = private_key

print(username, password)


session = requests.Session()

session.auth = (username, password)

session.headers.update({'ClientId': get_secret("cw-client-id")})

def get_cw_session():
    return session