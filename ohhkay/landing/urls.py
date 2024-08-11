from django.urls import path
from . import views

app_name = "landing"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("links/", views.LinksView.as_view(), name="links"),
    path("recommendations/", views.RecommendationsView.as_view(), name="recommendations"),
    path("privacy-policy/", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("imprint/", views.ImprintView.as_view(), name="imprint"),
]
