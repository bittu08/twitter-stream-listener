from tweetlistener.models import common
from tastypie.resources import Resource, ModelResource

class TweetListenerBaseResource(ModelResource):
    def determine_format(self, request):
        return 'application/json'
    
class KeywordResources(TweetListenerBaseResource):
    class Meta:
        queryset = common.KeywordData.objects.all()
        resource_name = 'keywords'