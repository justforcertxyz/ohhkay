from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path("<slug:slug>", views.BlogDetailView.as_view(), name="detail"),
]
