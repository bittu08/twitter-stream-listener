from tweetlistener.models import common
from tastypie.resources import Resource, ModelResource
from tastypie.authorization import Authorization
from django.conf.urls import url

class TwitterBaseResource(ModelResource):
	def __init__(self, data_source = None, *args, **kwargs):
		super(TwitterBaseResource, self).__init__(*args, **kwargs)
		self.dao = data_source
	
	def determine_format(self, request):
		return 'application/json'

class KeywordResources(TwitterBaseResource):
    class Meta:
        queryset = common.KeywordData.objects.all()
        resource_name = 'keywords'
        authorization= Authorization()	


class TwitterResource(TwitterBaseResource):
	class Meta:
		resource_name = 'tweets'
		authorization= Authorization()

	def obj_get_list(self, bundle, **kwargs):
		data = self.dao.get_list()
		for obj in data:
			print obj['pk']
		return data

	def obj_get(self, bundle, **kwargs):
		id = kwargs.get('id', None)
		return self.dao.get(id=id)

class TwitterSearchResource(TwitterBaseResource):
    class Meta:
        resource_name = 'search'

    def base_urls(self):
        return [
            url(r"^tweets/search", self.wrap_view('dispatch_search'))
        ]

    def dispatch_search(request, **kwargs):
    	free_text = request.get.GET['q']
    	user_name = request.get.GET['user_name']
    	data = self.get_search_result(free_text=free_text, user_name=user_name)
    	to_be_serialized = {"data": data}
        return self.create_response(request, data=to_be_serialized)

    def get_search_result(self, free_text=None, user_name=None, *args, **kwargs):
    	pass