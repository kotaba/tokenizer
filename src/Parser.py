import urllib, json
from config.api import ApiConfig
from MongoDB import Database
'''
Component for parse meetmix api and get events data
'''

class Parse:

	def __init__(self):
		self.api_config = ApiConfig()
		mongodb = Database()
		self.db = mongodb.get_connection()

	# make json request to specific url
	def json_request(self, url):
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		return data

	def get_parse_urls(self):
		base_url = self.api_config.param('meetmix_api_url')
		urls = []
		for i in range(1, 1000):
			url = base_url + '/event/' + str(i)
			urls.append(url)
		return urls	

	def proccess_urls(self):
		urls = self.get_parse_urls()
		for url in urls:
			data = self.json_request(url)
			print data['id']

			

