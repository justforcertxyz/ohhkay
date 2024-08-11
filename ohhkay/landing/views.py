from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "landing/index.html"


class LinksView(TemplateView):
    template_name = "landing/links.html"


class RecommendationsView(TemplateView):
    template_name = "landing/recommendations.html"


class PrivacyPolicyView(TemplateView):
    template_name = "landing/privacy_policy.html"


class ImprintView(TemplateView):
    template_name = "landing/imprint.html"
