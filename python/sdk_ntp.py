#!/usr/bin/env python3

import intersight
import re
from pprint import pprint
from intersight.api import organization_api
from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship
from intersight.api import ntp_api
from intersight.model.ntp_policy import NtpPolicy

def get_api_client(api_key_id, api_secret_file, endpoint="https://intersight.com"):
    with open(api_secret_file, 'r') as f:
        api_key = f.read()

    if re.search('BEGIN RSA PRIVATE KEY', api_key):
        # API Key v2 format
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
        signing_scheme = intersight.signing.SCHEME_RSA_SHA256
        hash_algorithm = intersight.signing.HASH_SHA256

    elif re.search('BEGIN EC PRIVATE KEY', api_key):
        # API Key v3 format
        signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
        signing_scheme = intersight.signing.SCHEME_HS2019
        hash_algorithm = intersight.signing.HASH_SHA256

    configuration = intersight.Configuration(
        host=endpoint,
        signing_info=intersight.signing.HttpSigningConfiguration(
            key_id=api_key_id,
            private_key_path=api_secret_file,
            signing_scheme=signing_scheme,
            signing_algorithm=signing_algorithm,
            hash_algorithm=hash_algorithm,
            signed_headers=[
                intersight.signing.HEADER_REQUEST_TARGET,
                intersight.signing.HEADER_HOST,
                intersight.signing.HEADER_DATE,
                intersight.signing.HEADER_DIGEST,
            ]
        )
    )
    # if you want to turn off certificate verification
    # configuration.verify_ssl = False

    return intersight.ApiClient(configuration)

def get_orgs(api_client):
    # Enter a context with an instance of the API client
    with api_client:
        # Create an instance of the API class
        api_instance = organization_api.OrganizationApi(api_client)
        try:
            # Read a Organization resource.
            api_response = api_instance.get_organization_organization_list(filter="Name eq 'default'")
        except intersight.ApiException as e:
            print("Exception when calling OrganizationApi -> get_organization_organization_list: %s\n" % e)
    return api_response.results[0]


def get_organization_rel(moid):
    # Creating an instance of organization
    organization = OrganizationOrganizationRelationship(class_id="mo.MoRef",
        object_type="organization.Organization",
        moid=moid)
    return organization


if __name__ == '__main__':
    # Api Client
    with open('../ApiKey.txt', 'r') as f:
        ApiKey = f.read()

    api_client = get_api_client(ApiKey, "../SecretKey.txt")

    # Create an api instance of the correct API type
    api_instance = ntp_api.NtpApi(api_client)

    # Get Organization Info
    Orgs = get_orgs(api_client)
    OrgRel = get_organization_rel(Orgs.moid)

    # NTP Policy Object with desired configuration
    ntp_policy = NtpPolicy(name="pysdk_demo",
                            description="Demo NTP Policy using Python SDK",
                            timezone="America/Los_Angeles",
                            enabled=True,
                            ntp_servers=[ "8.8.8.8", "8.8.4.4"],
                            organization=OrgRel
                        )

    try:
        # Create NTP Policy
        api_response = api_instance.create_ntp_policy(ntp_policy)
        pprint(api_response)
    except intersight.ApiException as e:
        print("Exception when calling BootApi->create_boot_precision_policy: %s\n" % e)
