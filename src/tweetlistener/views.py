from django.http import HttpResponse

def home(request):
	return HttpResponse(content='Welcome to Twitter stream listener')