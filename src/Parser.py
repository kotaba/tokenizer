import urllib, json
from config.api import ApiConfig
from MongoDB import Database
import datetime
import sys
from threading import Thread
'''
Component for parse meetmix api and get events data
'''

class Parse:

	def __init__(self):
		self.api_config = ApiConfig()
		mongodb = Database()
		self.db = mongodb.get_connection()
		self.total_items = 0

	# make json request to specific url
	def json_request(self, url):
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		return data

	def get_parse_urls(self):
		base_url = self.api_config.param('meetmix_api_url')
		cities_ids = self.api_config.param('active_cities')
		date = datetime.datetime.today().strftime('%Y-%m-%d')
		urls = []
		for city_id in cities_ids:
			url = base_url + '/events/' + str(city_id) + '/' + date
			urls.append(url)
		return urls

	def proccess_urls(self):
		urls = self.get_parse_urls()
		collection_src = self.db.src_data
		collection_log = self.db.log_data
		log_item = {
				'run_at': datetime.datetime.today(),
				'urls': urls
			}
		for url in urls:
			# make thread for each url
			tr = Thread(target=self.proccess_single_url, args=(url, collection_src))
			tr.start()
		print 'Finished. Total items write: ' + str(self.total_items)
		log_item['end_at'] = datetime.datetime.today()
		log_item['write_items'] = self.total_items
		log_item['run_time'] = str(log_item['end_at'] - log_item['run_at'])
		collection_log.insert_one(log_item)

	def proccess_single_url(self, url, collection):
		total = 0;
		print 'Parse start [' + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ']'
		print 'Url: ' + url
		data = self.json_request(url)
		counter = 0
		one_total = len(data)
		tr = Thread(target=self.save_parse_data, args=(collection, item))
		tr.start()

	def save_parse_data(self, collection, item):
		item = {'event_id': item['id'], 
							'created_at': datetime.datetime.today(), 
							'title': item['name'], 
							'description': item['description']
							}
		collection.insert_one(item)


			

