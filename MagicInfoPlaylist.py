from typing import *
from utils.http_requests import *

class MagicInfoPlaylist:

	def __init__(self):
		self.playlist_base_url = 'http://35.203.55.238:7001/MagicInfo/restapi/v1.0/cms/playlists'

	def get_playlists(self, startIndex=1, pageSize=10) -> List:
		url = self.playlist_base_url + f'?startIndex={startIndex}&pageSize={pageSize}'
		contents = get_playlists_request(url).playlists
		return contents

	def create_playlist(self, content_list: List[str]) -> None:
		url = self.playlist_base_url
		content_list = [{'contentId': content} for content in content_list]
		response = create_playlist_request(url, content_list)
		print(response.status)

# [('EB08268D-C6F7-4A11-94CF-8E3F2B5EA7C8', 'test-img'), ('442AD792-0E7B-440C-9213-C0E7F5EAC06D', 'test-img'), ('7313EF7F-2352-428B-8F94-D494C990AB7A', 'test-img'), ('F5A2B093-2D00-405C-A4DE-417678279770', 'MyContent_2003111723.LFD'), ('90F4AB4A-191A-4C6C-8AAD-E522D748C017', '20200219_094721'), ('19287829-41BD-458B-8BFC-E0ABAB9B71CF', 'MagicInfo 7 Introduction_20190305'), ('D51524B3-075F-4013-8E7D-13BCB1F1F707', 'surprised pikachu')]
c = MagicInfoPlaylist()
# print(c.get_playlists())
c.create_playlist(['EB08268D-C6F7-4A11-94CF-8E3F2B5EA7C8', 'F5A2B093-2D00-405C-A4DE-417678279770'])

# PlaylistResource
# {
# 	categoryList(Array[Inline
# Model
# 1], optional),
# contentCount(integer),
# contentList(Array[PlaylistItemResource], optional),
# creatorId(string),
# deviceType(string),
# deviceTypeVersion(string),
# groupId(string),
# groupName(string),
# lastModifiedDate(string),
# metaData(string),
# playTime(integer),
# playlistId(string, optional),
# playlistName(string),
# playlistType(string),
# shareFlag(integer),
# shuffleFlag(string),
# thumbFileName(string, optional),
# thumbFilePath(string, optional),
# totalSize(integer, optional),
# versionId(integer)
# }Inline
# Model
# 1
# {}
# PlaylistItemResource
# {
# 	contentDuration(integer, optional),
# 	contentDurationMilli(string, optional),
# 	contentId(string),
# 	contentName(string, optional),
# 	contentOrder(integer, optional),
# 	expiredDate(string, optional),
# 	hasDefaultPlayTime(boolean, optional),
# 	mediaType(string, optional),
# 	playTime(string, optional),
# 	playlistId(string, optional),
# 	resolution(string, optional),
# 	startDate(string, optional),
# 	subPlaylist(boolean, optional),
# 	tagList(string, optional),
# 	tagMatchType(string, optional),
# 	tagValue(string, optional),
# 	thumbFileId(string, optional),
# 	thumbFileName(string, optional),
# 	thumbFilePath(string, optional),
# 	versionId(integer, optional)
# }