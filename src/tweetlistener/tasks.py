from __future__ import absolute_import
from celery import shared_task
from django.conf import settings
from listener.streaming import TwitterHandler

"""
This job send the twitter stream into elasticsearch
"""
@shared_task
def send_tweet_stream_to_elasticsearch(*args, **kwargs, data = None):
    try:
        obj = TwitterHandler(keywords = keywords, **settings.TWITTER_CONFIG)
        obj.handler()
    except (Exception) as ex:
        print "Caught exception:{0}".format(ex)