from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Context
from django.template.loader import get_template

from post_service.models import Post


def post_list(request):
    template = get_template('post_list.html')
    context = Context({'hello_world_arg':'JHJR','post_list': Post.objects.all()})
    return HttpResponse(template.render(context))

    # return render(request, 'post_list.html',{'hello_world_arg':'JHJR1'} )




