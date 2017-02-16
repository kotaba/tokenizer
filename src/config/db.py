from config import Config

class DbConfig(Config):

	def __init__(self):
		self.data = {
			'mongodb_host': '146.148.28.57',
			'mongodb_user': 'python',
			'mongodb_password': '12345',
			'mongodb_port' : 27017,
			'mongodb_database' : 'main'
		}
