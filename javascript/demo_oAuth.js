#
#  Install node-fetch library: npm install node-fetch
#  Run script: node --experimental-modules oauth.js
#
import fetch from 'node-fetch';

async function getToken(clientId, clientSecret) {
  const tokenUrl = 'https://intersight.com/iam/token';
  const clientAuth = Buffer.from(`${clientId}:${clientSecret}`).toString('base64');
  const postData = { grant_type: 'client_credentials' };
  const response = await fetch(tokenUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      Authorization: `Basic ${clientAuth}`
    },
    body: new URLSearchParams(postData)
  });

  if (response.status !== 200) {
    console.error('Failed to obtain token from the OAuth 2.0 server');
    process.exit(1);
  }

  console.log('Successfully obtained a new token');
  const tokenJson = await response.json();
  return tokenJson.access_token;
}

async function getApiData(token, clientId, clientSecret, apiUrl) {
  const headers = { Authorization: `Bearer ${token}` };
  const response = await fetch(apiUrl, {
    headers
  });

  if (response.status === 401) {
    console.log('Existing Token Expired. Generating a new one!');
    token = await getToken(clientId, clientSecret);
    await getApiData(token, clientId, clientSecret, apiUrl);
  } else {
    const data = await response.json();
    console.log(data);
  }
}

// Set variables
const clientId = 'xxxx'; // Update
const clientSecret = 'xxxx'; // Update
const apiUrl =
  "https://intersight.com/api/v1/organization/Organizations?$filter=Name eq 'default'&$select=Name,Description"; // Update

// Get OAuth Token
getToken(clientId, clientSecret)
  .then((token) => {
    // Get API Endpoint Data
    getApiData(token, clientId, clientSecret, apiUrl);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
