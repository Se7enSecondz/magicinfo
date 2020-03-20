from utils import generate_token
from utils.content_response_handler import ContentResponseHandler
from utils.playlist_response_handler import PlaylistResponseHandler
import requests


def build_kwargs(url, json=None, headers=None, file=None):
	return {
		'url': url,
		'json': {} if json is None else json,
		'headers': {
			'api_key': generate_token()
		} if headers is None else headers,
		'files': {
			'file': open(file, 'rb') if file else None
		}
	}

def get_contents_request(url: str) -> ContentResponseHandler:
	kwargs = build_kwargs(url)
	return ContentResponseHandler(requests.get(**kwargs))

def delete_content_request(url: str) -> ContentResponseHandler:
	kwargs = build_kwargs(url)
	return ContentResponseHandler(requests.delete(**kwargs))

def upload_content_request(url: str, content: str) -> ContentResponseHandler:
	kwargs = build_kwargs(url, file=content)
	return ContentResponseHandler(requests.post(**kwargs))

def get_playlists_request(url: str) -> PlaylistResponseHandler:
	kwargs = build_kwargs(url)
	return PlaylistResponseHandler(requests.get(**kwargs))

def create_playlist_request(url: str, content_list):
	kwargs = build_kwargs(url, json={'contentList': content_list})
	return PlaylistResponseHandler(requests.post(**kwargs))
