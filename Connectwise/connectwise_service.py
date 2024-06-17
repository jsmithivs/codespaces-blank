from sys import gettrace
import requests
from Connectwise.kv_secrets import get_secret
from Connectwise.connectwise_api_configuration import get_cw_session

base_url = "https://connect.iventuresolutions.com/v4_6_release/apis/3.0/"

session = get_cw_session()

response = session.get(f"{base_url}service/tickets")

print(response.status_code)
print(response.json())

"""
https://developer.connectwise.com/Products/ConnectWise_PSA/REST#/AgreementAdditions/patchFinanceAgreementsByParentIdAdditionsById
"""
def PatchAgreementAddition(agreement_id: int, addition_id: int, request: dict):
    response = session.patch(f"{base_url}finance/agreements/{agreement_id}/additions/{addition_id}", request)
    return response.json()

