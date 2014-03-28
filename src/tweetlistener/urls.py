from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from tweetlistener.resource import resources as r 

api_v1 = Api(api_name="v1")
api_v1.register(r.KeywordResources())

urlpatterns = patterns('tweetlistener',
	(r'', include(api_v1.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^home/','views.home', name='home'),
)
