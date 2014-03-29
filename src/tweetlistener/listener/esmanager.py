from elasticsearch import Elasticsearch
from tweetlistener.utils import import_json
import logging

logger = logging.getLogger(__name__)
json = import_json()

fetch_source = lambda iterator: [obj['_source'] for obj in iterator]

class ElasticSearchManager(object):

	def __init__(self, index=None, doc_type=None, *args, **kwargs):
		self.index = index
		self.doc_type = doc_type
		self.obj_es = Elasticsearch()

	def search(self, search_text = None, *args, **kwargs):
		data = self.obj_es.search(index=self.index, doc_type=self.doc_type, body={"query":{"match":{"text":search_text}}})
		return fetch_source(data['hits']['hits'])

	def get(self, *args, **kwargs):
		data=self.obj_es.get(index=self.index, doc_type=self.doc_type, id=kwargs['id'])
		return data['_source']

	def get_list(self, *args, **kwargs):
		data = self.obj_es.search(index=self.index, body={"query": {"match_all": {}}})
		return fetch_source(data['hits']['hits'])

	def insert(self, data = None):
		data = json.loads(data)
		data['user_name'] = data['user']['screen_name']
		del data['user']
		del data['entities']
		res = self.obj_es.index(index=self.index, doc_type=self.doc_type, id=data['id'], body=data)
		logger.info("Getting stream:{0}".format(res))

	def delete(self, data = None):
		pass

	def update(self, data = None):
		pass

