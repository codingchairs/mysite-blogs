from django.http import HttpResponse
from django.views.generic import TemplateView


class Home(TemplateView):
	template_name = 'home.html'

def hello(request):
	return HttpResponse("Hello World")