import requests
import os


# Get secrets from Vault
def get_secret(server, path, folder, token): 
    try:
        response = requests.get(
            url=f'https://{server}/v1/{path}/data/{folder}',
            headers={
                "Content-Type": "application/json",
                "X-Vault-Token": token
            }
        )
    except requests.exceptions.RequestException as e:
        print(e)
        raise

    if response.ok:
        secrets = response.json()["data"]["data"]
        return secrets
    else:
        raise Exception("status_code={0}, message={1}".format(response.status_code, response.json()))

# Get secrets from Vault
secrets = get_secret(
    server = os.environ.get("VAULT_QA_SERVER"),
    path   = os.environ.get("VAULT_PATH"), 
    folder = os.environ.get("VAULT_FOLDER"),
    token  = os.environ.get("VAULT_TOKEN")
)

# Endpoint
chkpt = {
    "main_url" :   'https://cloudinfra-gw.portal.checkpoint.com/app/endpoint-web-mgmt/harmony/endpoint/api',
    "auth_url" :   secrets['cp_auth_url'],
    "client_id" :  secrets['cp_client_id'],
    "secret_key" : secrets['cp_secret_key'],
}

# Search group
group_id = os.environ.get("GROUP_ID")