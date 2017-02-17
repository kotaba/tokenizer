from config import Config

class ApiConfig(Config):

	def __init__(self):
		self.data = {
			'meetmix_api_url': 'http://api.meetmix.ru',
			'active_cities': [314, 282, 652, 650]
		}