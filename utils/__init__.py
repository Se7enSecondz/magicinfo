import requests

AUTH_URL = 'http://35.203.55.238:7001/MagicInfo/auth'
USERNAME = 'admin'
PASSWORD = 'magicinfo123!'

def generate_token():
	url = AUTH_URL
	r = requests.post(
		url=url,
		json={
			'username': USERNAME,
			'password': PASSWORD
		}
	)
	return r.json()['token']

# print(generate_token())
