from django.http import HttpResponse

def home(request):
	return HttpResponse(content='Hello World')



