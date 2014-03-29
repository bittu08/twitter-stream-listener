from elasticsearch import Elasticsearch
import json

class ElasticSearchHandler(object):

	def __init__(self, *args, **kwargs):
		self.es = Elasticsearch()

	def insert(self, data = None):
		data = json.loads(data)
		data['user_name'] = data['user']['screen_name']
		del data['user']
		del data['entities']
		res = self.es.index(index="twitter", doc_type='tweet', id=data['id'], body=data)
		print res
