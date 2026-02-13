import requests

headers = {

    'Authorization': 'Token {$DEFECTDOJO_API_KEY}'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': 'Gitleads Scan',
    'minimum_severity': 'Low',
    'engagement': 20
}

files = {
    'file': open('gitleaks.json', 'rb')

}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan result successful')
else:
    print(f'Failed scan: {response.content}')