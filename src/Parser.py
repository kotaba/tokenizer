import urllib, json
from config.api import ApiConfig
from MongoDB import Database
import datetime
import sys
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
		cities_ids = self.api_config.param('active_cities')
		date = datetime.datetime.today().strftime('%Y-%m-%d')
		urls = []
		for city_id in cities_ids:
			url = base_url + '/events/' + str(city_id) + '/' + date
			urls.append(url)
		return urls

	def proccess_urls(self):
		total = 0;
		urls = self.get_parse_urls()
		collection_src = self.db.src_data
		collection_log = self.db.log_data
		log_item = {
				'run_at': datetime.datetime.today(),
				'urls': urls
			}
		for url in urls:
			print 'Parse start [' + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ']'
			print 'Url: ' + url
			data = self.json_request(url)
			counter = 0
			one_total = len(data)
			for item in data:
				if not collection_src.find_one({"event_id": item['id']}):
					item = {'event_id': item['id'], 
							'created_at': datetime.datetime.today(), 
							'title': item['name'], 
							'description': item['description']
							}
					collection_src.insert_one(item)
					counter = counter + 1
					total = total + 1;
				else:
					one_total = one_total - 1
				print 'Items ' + str(counter) + '/' + str(one_total)		
		print 'Finished. Total items write: ' + str(total)
		log_item['end_at'] = datetime.datetime.today()
		log_item['write_items'] = total
		log_item['run_time'] = str(log_item['end_at'] - log_item['run_at'])
		collection_log.insert_one(log_item)		

			

