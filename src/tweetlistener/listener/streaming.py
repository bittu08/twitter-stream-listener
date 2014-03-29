from tweepy.streaming import StreamListener
from tweetlistener.exception import ListenerError
import logging

logger = logging.getLogger(__name__)

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
        try:
            self.dao.insert(data = data)
        except Exception as ex:
            logger.exception("Error occured on stream data receiving: {0}".format(ex))
            return False
        return True

    def on_error(self, status):
        error_message = "Encountered error with status code: {0}".format(status)
        logger.info(error_message)
        raise ListenerError(error_message)