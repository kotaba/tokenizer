from pymongo import MongoClient
from config.db import DbConfig

class Database:
	def __init__(self):
		config = DbConfig()
		connection = MongoClient(config.param('mongodb_host'))
		connection.main.authenticate(config.param('mongodb_user'), config.param('mongodb_password'))
		self.db = connection.main
	
	def get_connection(self):
		return self.db