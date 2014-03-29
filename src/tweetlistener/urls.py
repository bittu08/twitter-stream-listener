from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from tweetlistener.resource import resources as r 
from tweetlistener.listener import esmanager as esm

api_v1 = Api(api_name="v1")
api_v1.register(r.KeywordResources())
api_v1.register(r.TwitterResource(data_source = esm.ElasticSearchManager(**settings.TWITTER_CONFIG)))
api_v1.register(r.TwitterSearchResource(data_source = esm.ElasticSearchManager(**settings.TWITTER_CONFIG)))

urlpatterns = patterns('tweetlistener',
	(r'', include(api_v1.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^','views.home', name='home'),
)
