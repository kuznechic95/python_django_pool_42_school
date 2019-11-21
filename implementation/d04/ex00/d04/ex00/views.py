from django.shortcuts import render
from django.views.generic import TemplateView

class IndexPageView(TemplateView):
    template_name = 'index.html'