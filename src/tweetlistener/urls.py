from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('tweetlistener',
    # Uncomment the next line to enable the admin:
    url(r'^home/','views.home', name='home'),
)
