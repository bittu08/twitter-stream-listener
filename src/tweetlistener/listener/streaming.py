from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from esmanager import ElasticSearchManager


"""
A Twitter listener, its capture all the tweet from keyword list
"""
class TwitterListener(StreamListener):

    def __init__(self, dao=None, *args, **kwargs):
        super(TwitterListener, self).__init__(*args, **kwargs)
        self.dao = dao

    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        self.dao.insert(data = data)
        return True

    def on_error(self, status):
        print status

class TwitterHandler(object):

    def __init__(self, keywords=[], *args, **kwargs):
        self.keywords = keywords
        self.consumer_key = kwargs.get('consumer_key', None)
        self.consumer_secret = kwargs.get('consumer_secret', None)
        self.access_token = kwargs.get('access_token', None)
        self.access_token_secret = kwargs.get('access_token_secret',  None)
        self.index = kwargs.get('index', None)
        self.doc_type = kwargs.get('doc_type', None)

    def handler(self):
        esm = ElasticSearchManager(index=self.index , doc_type = self.doc_type)
        obj_listener = TwitterListener(dao=esm)
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        stream = Stream(auth, obj_listener)
        stream.filter(track=self.keywords)