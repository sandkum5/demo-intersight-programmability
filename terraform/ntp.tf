terraform {
  required_version = ">= 1.13.3"
  required_providers {
    intersight = {
      source  = "CiscoDevNet/intersight"
      version = "1.0.69"
    }
  }
}

provider "intersight" {
  apikey    = file("./ApiKey.txt")
  secretkey = "./SecretKey.txt"
  endpoint  = "https://intersight.com"
}

data "intersight_organization_organization" "org_data" {
  name = "default"
}

resource "intersight_ntp_policy" "ntp_policy" {
  name        = "tf_ntp"
  description = "Policy Created using terraform"
  enabled     = true
  ntp_servers = ["1.1.1.1", "2.2.2.2"]
  timezone    = "America/Los_Angeles"
  organization {
    object_type = "organization.Organization"
    moid = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = "DC"
    value = "LAB"
  }
}

output "ntp_data" {
  value = intersight_ntp_policy.ntp_policy
}
