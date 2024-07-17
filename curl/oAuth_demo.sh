# Request:
curl -u "$clientId:$clientSecret" -H 'Content-Type: application/json' -X POST https://intersight.com/iam/token -d '{"grant_type": "client_credentials"}'

# Response:
# {"access_token":"xxxx","expires_in":600,"token_type":"Bearer"}

# Request:
curl -X GET -H "Authorization: Bearer $access_token" -H 'Content-Type: application/json' $url
