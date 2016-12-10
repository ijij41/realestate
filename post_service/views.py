from django.shortcuts import render

# Create your views here.
from django.template import Context
from django.template.loader import get_template


def post_list(request):
    template = get_template('post_list.html')
    context = Context({})
    return template.render(context)


