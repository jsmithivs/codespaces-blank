from sys import gettrace
import requests
from kv_secrets import get_secret

def is_debugging():
    return gettrace() is not None

public_key = get_secret("cw-public-key")
private_key = get_secret("cw-private-key")

username = f"training+{public_key}" if is_debugging() else f"iventure+{public_key}"
password = private_key

print(username, password)

baseurl = "https://connect.iventuresolutions.com/v4_6_release/apis/3.0/"

session = requests.Session()

session.auth = (username, password)

session.headers.update({'ClientId': get_secret("cw-client-id")})

response = session.get(f"{baseurl}service/tickets")

print(response.status_code)
print(response.json())