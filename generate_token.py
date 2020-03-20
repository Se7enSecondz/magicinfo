import json
import requests

from typing import ByteString

def generate_token():
	with open('utils/api_key.txt') as f:
		return f.read()
#
# def generate_token():
# 	url = 'http://35.203.55.238:7001/MagicInfo/auth'
# 	r = requests.post(
# 		url=url,
# 		json={
# 			'username': 'admin',
# 			'password': 'magicinfo123!'
# 		}
# 	)
# 	# print(json.loads(r.content)['token'])
# 	return json.loads(r.content)['token']

def get_playlists():
	url = 'http://35.203.55.238:7001/MagicInfo/restapi/v1.0/cms/playlists?startIndex=1&pageSize=10'
	r = requests.get(
		url=url,
		headers={
			'api_key': generate_token(),
			'Accept': 'application/json'
		}
	)
	print(r.text)

def get_contents():
	url = 'http://35.203.55.238:7001/MagicInfo/restapi/v1.0/cms/contents?startIndex=1&pageSize=10'
	r = requests.get(
		url=url,
		headers={
			'api_key': generate_token(),
			'Accept': 'application/json'
		}
	)
	print(r.text)

def refresh_token():
	url = 'http://35.203.55.238:7001/MagicInfo/auth/refresh'
	r = requests.get(
		url=url,
		headers={
			'api_key': generate_token()
		},
		json={
			'username': 'admin',
			'password': 'magicinfo123!'
		}
	)
	print(r.text)

def upload_content(group_id: str):
	url = f'http://35.203.55.238:7001/MagicInfo/restapi/v1.0/cms/contents/{group_id}'
	r = requests.post(
		url=url,
		headers={
			'api_key': generate_token()
		},
		files={
			'file': open('/home/chris/Pictures/test-img.jpg', 'rb')
		}
	)
	print(r.text)

def list_default_group():
	url = 'http://35.203.55.238:7001/MagicInfo/restapi/v1.0/cms/contents/groups'
	r = requests.get(
		url=url,
		headers={
			'api_key': generate_token()
		}
	)
	print(r.text)

# list_default_group()

upload_content(0)
# get_contents()
# refresh_token()
# get_playlists()