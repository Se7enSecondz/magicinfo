from typing import List
from utils.http_requests import *

class ContentController:

	def __init__(self):
		self.contents_base_url = 'http://35.203.55.238:7001/MagicInfo/restapi/v1.0/cms/contents'

	def get_contents(self, startIndex=1, pageSize=10) -> List:
		url = self.contents_base_url + f'?startIndex={startIndex}&pageSize={pageSize}'
		contents = get_contents_request(url).contents
		return contents

	def upload_content(self, content: str, groupId: int = 0) -> None:
		url = self.contents_base_url + f'/{groupId}'
		response = upload_content_request(url, content)
		print(f'Upload status: {response.status}')

	def delete_content(self, contentId: str) -> None:
		url = self.contents_base_url + f'/{contentId}'
		response = delete_content_request(url)
		print(f'Delete status: {response.status}')


c = ContentController()
print(c.get_contents())
# c.upload_content('/home/chris/Pictures/test-img.jpg', 0)
# c.delete_content('274050A4-7A17-4723-AB4B-9A30935EB25asd')
