from typing import *
import requests


class PlaylistResponseHandler:

	def __init__(self, response: requests.Response) -> None:
		self.response = response

	@property
	def status(self) -> str:
		return self.response.json()['status']

	@property
	def playlists(self) -> List:
		items = self.response.json()['items']
		playlists = [(item['playlistId'], item['playlistName']) for item in items]
		return playlists
