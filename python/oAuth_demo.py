#!/usr/bin/env python3
"""
    Intersight API calls using oAuth
"""

import sys
import requests
from pprint import pprint

def get_token(client_id, client_secret):
    """ Get oAuth Token """
    token_url="https://intersight.com/iam/token"
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    post_data = {"grant_type": "client_credentials"}
    response = requests.post(url=token_url,
                            auth=client_auth,
                            data=post_data)
    if response.status_code != 200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)
    print("Successfuly obtained a new token")
    token_json = response.json()
    return token_json["access_token"]

def get_org(token, client_id, client_secret):
    """ Get Organization Info """
    api_url = "https://intersight.com/api/v1/organization/Organizations?$filter=Name eq 'default'"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url=api_url, headers=headers)
    if	response.status_code == 401:
        token = get_token(client_id, client_secret)
        get_org(token, client_id, client_secret)
    else:
        pprint(response.json())

if __name__ == '__main__':
    # Set variables
    client_id = "Add Client ID"    # Update
    client_secret = "Add Client Secret" # Update

    # Get oAuth Token
    token = get_token(client_id, client_secret)

    # Get Organization Info
    get_org(token, client_id, client_secret)
