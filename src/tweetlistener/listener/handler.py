from tweepy import OAuthHandler
from tweepy import Stream
from esmanager import ElasticSearchManager
from tweetlistener.models import common
from streaming import TwitterListener
import time

class TwitterHandler(object):

    def __init__(self, async_time = 3600, *args, **kwargs):
        self.consumer_key = kwargs.get('consumer_key', None)
        self.consumer_secret = kwargs.get('consumer_secret', None)
        self.access_token = kwargs.get('access_token', None)
        self.access_token_secret = kwargs.get('access_token_secret',  None)
        self.index = kwargs.get('index', None)
        self.doc_type = kwargs.get('doc_type', None)
        self.async_time = async_time

    def handler(self):
        esm = ElasticSearchManager(index=self.index , doc_type = self.doc_type)
        obj_listener = TwitterListener(dao=esm)
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        stream = Stream(auth, obj_listener)
        while True:
            if stream.running:
                stream.disconnect()
            keywords = self.get_keyword_list()
            stream.filter(track=keywords,async=True)
            time.sleep(self.async_time)

    def get_keyword_list(self):
        resultset = common.KeywordData.objects.filter(is_active=True)
        keywords = [data.keyword for  data in resultset]
        return keywords