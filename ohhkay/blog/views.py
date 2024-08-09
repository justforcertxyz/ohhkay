from django.shortcuts import render


class IndexListView(ListView):
    model = Blog
    template_name = "blog/index.html"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/detail.html"