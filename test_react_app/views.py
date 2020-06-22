from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "home.html"
