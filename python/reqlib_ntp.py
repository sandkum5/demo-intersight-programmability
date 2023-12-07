#!/usr/bin/env python3
"""
    Prerequisites:
    - Intersight Authentication helper library for requests
        pip install intersight-auth
"""
import requests
from intersight_auth import IntersightAuth
from pprint import pprint

def get_org(AUTH):
    """
        Get Organization info
    """
    HEADERS = {"Content-Type": "application/json"}
    URL = "https://intersight.com/api/v1/organization/Organizations?$filter=Name eq 'default'"
    response = requests.get(url=URL, auth=AUTH, headers=HEADERS)
    return response.json()

def create_ntp_policy(AUTH,orgMoid):
    HEADERS = {"Content-Type": "application/json"}
    URL = "https://intersight.com/api/v1/ntp/Policies"
    DATA = {
        "Organization": {
            "ObjectType": "organization.Organization",
            "Moid": orgMoid
        },
        "Name": "pyreq_demo",
        "Description": "Demo NTP Policy created using Python Request library",
        "Enabled": True,
        "NtpServers": [
            "8.8.8.8",
            "8.8.4.4"
        ],
        "Timezone": "America/Los_Angeles",
        "Tags": []
    }
    response = requests.post(url=URL, auth=AUTH, headers=HEADERS, json=DATA)
    return response

if __name__ == '__main__':
    # Intersight AUTH
    with open('../ApiKey.txt', 'r') as f:
        ApiKey = f.read()

    AUTH = IntersightAuth(
        secret_key_filename="../SecretKey.txt",
        api_key_id=ApiKey
    )
    # Get Org Moid
    orgInfo = get_org(AUTH)
    orgMoid = orgInfo['Results'][0]['Moid']

    # Create NTP Policy
    response = create_ntp_policy(AUTH,orgMoid)
    pprint(f"Response Status Code: {response.status_code}")
    pprint(response.json())
