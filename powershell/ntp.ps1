$ApiParams = @{
    BasePath = "https://intersight.com"
    ApiKeyId = Get-Content -Path "/Users/sandkum5/Documents/automation/podman/demos/ApiKey.txt" -Raw
    ApiKeyFilePath = "/Users/sandkum5/Documents/automation/podman/demos/SecretKey.txt"
    HttpSigningHeader = @("(request-target)", "Host", "Date", "Digest")
}

Set-IntersightConfiguration @ApiParams

$org = Get-IntersightOrganizationOrganization -Name "default"

$ntpPolicy = New-IntersightNtpPolicy -Name "Pwsh_Demo" -Description "ntp policy created using Powershell" -NtpServers @("22.22.22.22","77.77.77.77") -Enabled $true -Timezone IndianMauritius -Organization $org

$ntpPolicy
