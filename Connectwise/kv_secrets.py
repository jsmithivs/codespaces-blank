from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

KV_NAME = "billing-automation"
KV_Uri = f"https://{KV_NAME}.vault.azure.net/"

# Specify the tenant ID for the VisualStudioCodeCredential
credential = DefaultAzureCredential()

client = SecretClient(vault_url=KV_Uri, credential=credential)

def get_secret(secret_name: str):
    print(f"Retrieving your secret from {KV_NAME}.")
    retrieved_secret = client.get_secret(secret_name)
    print(f"Your secret is '{retrieved_secret.value}'.")
    return retrieved_secret.value
