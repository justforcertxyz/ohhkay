from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "landing/index.html"

class LinksView(TemplateView):
    template_name = "landing/links.html"