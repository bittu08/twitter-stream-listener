from __future__ import absolute_import
from celery import shared_task
from django.conf import settings
from tweetlistener.listener.streaming import TwitterHandler
from tweetlistener.models import common
import logging

logger = logging.getLogger(__name__)

"""
This job send the twitter stream into elasticsearch
"""
@shared_task
def send_tweet_stream_to_elasticsearch(*args, **kwargs):
    try:
        resultset = common.KeywordData.objects.filter(is_active=True)
        keywords = [data.keyword for  data in resultset]
        print keywords
        obj = TwitterHandler(keywords = keywords, **settings.TWITTER_CONFIG)
        obj.handler()
    except (Exception) as ex:
        logger.exception('Exception:{0}'.format(ex))