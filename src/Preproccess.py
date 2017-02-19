from MongoDB import Database
from Classifier import Classifier
from bson.code import Code
import json
import pprint

class Proccessor:

	def __init__(self):
		mongodb = Database()
		self.db = mongodb.get_connection()
		self.collection_src = self.db.src_data
		self.collection_indexes_tmp = self.db.indexes_tmp
		self.collection_words_count = self.db.words_count

	def find_data(self):
		data = []
		collection_data = self.collection_src.find()
		for item in collection_data:
			data.append(item['description'])
		return data
			
	def structurize_data(self):
		data = self.find_data()
		indexes = []
		i = 0
		for description in data:
			classificator = Classifier(description)
			classificator.make_structure()
			indexes.append(classificator.structure)
		classificator.make_words(indexes)
		self.collection_indexes_tmp.delete_many({})
		self.collection_indexes_tmp.insert_many(classificator.indexes)
		map = Code("function () {"
            			"  this.word.forEach(function(z) {"
            			"    emit(z, 1);"
            			"  });"
            			"}")
		reduce = Code("function (key, values) {"
	               		"  var total = 0;"
               			"  for (var i = 0; i < values.length; i++) {"
               			"    total += values[i];"
               			"  }"
              			"  return total;"
               			"}")
		result = self.collection_indexes_tmp.map_reduce(map, reduce, {'inline' : 1})
		self.collection_words_count.delete_many({})
		self.collection_words_count.insert_many(result['results'])





		