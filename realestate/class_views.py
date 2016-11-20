from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class TemplateTestView(TemplateView):
    template_name = "realestate/index.html"
