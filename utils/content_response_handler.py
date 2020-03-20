from typing import *
import requests


class ContentResponseHandler:

	def __init__(self, response: requests.Response) -> None:
		self.response = response

	@property
	def status(self) -> str:
		return self.response.json()['status']

	@property
	def contents(self) -> List:
		items = self.response.json()['items']
		contents = [(item['contentId'], item['contentName']) for item in items]
		return contents
