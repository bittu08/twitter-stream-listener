from tweetlistener.models import common
from tastypie.resources import Resource, ModelResource
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.utils.mime import determine_format, build_content_type
from django.conf.urls import url
from django.http import HttpResponse
from tweetlistener.utils import import_json
import logging

logger = logging.getLogger(__name__)
json=import_json()

class TwitterBaseResource(Resource):
	def __init__(self, data_source = None, *args, **kwargs):
		super(TwitterBaseResource, self).__init__(*args, **kwargs)
		self.dao = data_source
	
	def determine_format(self, request):
		return 'application/json'

class KeywordResources(ModelResource):
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
		bundle.data = data
		return data

	def obj_get(self, bundle, **kwargs):
		pk_id = kwargs.get('pk', None)
		return self.dao.get(id=pk_id)

	def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
		desired_format = self.determine_format(request)
		if isinstance(data, Bundle):
			serialized = data.obj
		elif isinstance(data, dict):
			serialized = [raw.obj for raw in data['objects']]
		return HttpResponse(content=json.dumps(serialized), content_type=build_content_type(desired_format))

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
