<#
    Create NTP Policy

    Pre-requisites:
    - PowerShell 7.3.3
    - Install Intersight Module
        Install-Module -Name Intersight.PowerShell
#>

# Intersight Environment Configuration
$ApiParams = @{
    BasePath = "https://intersight.com"
    ApiKeyId = Get-Content -Path "/Path/to/ApiKey.txt" -Raw
    ApiKeyFilePath = "/Path/to/SecretKey.txt"
    HttpSigningHeader = @("(request-target)", "Host", "Date", "Digest")
}

Set-IntersightConfiguration @ApiParams

# Get Organization Info
$org = Get-IntersightOrganizationOrganization -Name "default"

# Create NTP Policy
$ntpPolicy = New-IntersightNtpPolicy -Name "Pwsh_Demo" -Description "ntp policy created using Powershell" -NtpServers @("159.203.8.72","23.130.139.90") -Enabled $true -Timezone IndianMauritius -Organization $org

# Print Created NTP Policy
$ntpPolicy
