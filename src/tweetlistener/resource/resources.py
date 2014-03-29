from tweetlistener.models import common
from tastypie.resources import Resource, ModelResource

class TwitterResource(Resource):
    class Meta:
        resource_name = 'tweets'

    def base_urls(self):
        return [
            url(r"^tweets", self.wrap_view('dispatch_tweet'))
            url(r"^tweets/search", self.wrap_view('dispatch_search'))
        ]

    def dispatch_tweet(request, **kwargs):
    	pass
    def dispatch_search(request, **kwargs):
    	pass
    	
class TweetListenerBaseResource(ModelResource):
    def determine_format(self, request):
        return 'application/json'
    
class KeywordResources(TweetListenerBaseResource):
    class Meta:
        queryset = common.KeywordData.objects.all()
        resource_name = 'keywords'