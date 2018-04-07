from django.shortcuts import render

# Create your viewclass here.
from django.views.generic import TemplateView


class TemplateTestView(TemplateView):
    #template_name = "realestate/index.html"
    # template_name = "sb-realestate/index.html"
    template_name = "pages/index.html"
    #template_name = "pages/login.html"

