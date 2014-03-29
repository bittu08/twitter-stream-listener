from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from esmanager import ElasticSearchHandler
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="IN6zHMLbiYeWTRAG41IzEw"
consumer_secret="gtT8Wdz3wW5fhkL1VNHi8IXiVOj4Z6JUyxIk6jyMTU"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2416222890-QpC6kPa1fsbiADLxP0sPCf4wVF9zEa9wy5OTCbt"
access_token_secret="bDWTVW5FB0DvSdsQA22ryfFXQdAdGyap2utBDQyqN1XJ2"



class TwitterListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        es  = ElasticSearchHandler()
        es.insert(data = data)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = TwitterListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['basketball'])