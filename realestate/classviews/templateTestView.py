from django.shortcuts import render

# Create your classviews here.
from django.views.generic import TemplateView


class TemplateTestView(TemplateView):
    #template_name = "realestate/index.html"
    # template_name = "sb-realestate/index.html"
    template_name = "pages/index.html"