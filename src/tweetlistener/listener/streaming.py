from tweepy.streaming import StreamListener

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