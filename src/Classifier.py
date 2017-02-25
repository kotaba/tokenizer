#*-* coding: utf-8 *-*

import nltk
import json

class Classifier:
	def __init__(self, text):
		self.allow_tags = ["NN", "NNP"]
		self.structure = []
		self.tagged = []
		self.text = text

	def tokenize(self):
		try:
			tokens = nltk.word_tokenize(self.text)
			tagged = nltk.pos_tag(tokens)
			return tagged
		except:
			pass

	def make_tagged(self):
		data = self.tokenize()
		self.tagged = data

	def make_structure(self):
		self.make_tagged()
		if self.tagged:
			for item in self.tagged:
				item_word = item[0]
				item_tag = item[1]
				if item_tag in self.allow_tags:
					self.structure.append(item_word)					

	def make_words(self, data):
		i = 0
		result = []
		already_indexed = []
		for item in data:
			for word in item['structure']:
				result.append({'word': [word], 'event_id': item['event_id']})
				i = i+1
		self.indexes = result

	def print_tagged(self):
		print json.dumps(self.tagged, ensure_ascii=False).encode('utf8')
	def print_indexes(self):
		print json.dumps(self.indexes, ensure_ascii=False).encode('utf8')