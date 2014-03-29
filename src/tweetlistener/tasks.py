from __future__ import absolute_import
from celery import shared_task
from django.conf import settings
from tweetlistener.listener.handler import TwitterHandler
from tweetlistener.exception import TaskException
import logging

logger = logging.getLogger(__name__)

"""
This job send the twitter stream into elasticsearch
"""
@shared_task
def send_tweet_stream_to_elasticsearch(*args, **kwargs):
    try:
        obj = TwitterHandler(async_time = settings.TWEET_ASYNC_TIME, **settings.TWITTER_CONFIG)
        obj.handler()
        logger.info("Success: stream from twitter")
    except (Exception, TaskException) as ex:
        logger.exception('Exception:{0}'.format(ex))
