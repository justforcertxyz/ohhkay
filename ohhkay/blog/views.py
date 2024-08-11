from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog
from parler.views import TranslatableSlugMixin


class IndexListView(ListView):
    model = Blog
    template_name = "blog/index.html"


class BlogDetailView(TranslatableSlugMixin, DetailView):
    model = Blog
    template_name = "blog/detail.html"
