from django.core.management.base import BaseCommand, CommandError
from tweetlistener import tasks


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        tasks.send_tweet_stream_to_elasticsearch.delay()
        