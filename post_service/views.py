from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template

from post_service.models import Post


@login_required
# @permission_required('post_service.add_post', login_url="/login/")
def post_list(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('http://yahoo.com')
    # else:
    #     return HttpResponseRedirect('http://google.com')


    template = get_template('post_list.html')
    # context = Context({'hello_world_arg':'JHJR','post_list': Post.objects.all()})
    page_data = Paginator(Post.objects.all(), 5)
    # page = request.GET['page']
    page = request.GET.get('page')
    if page is None:
        page = 1

    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = Context({'post_list': posts, 'total_page': range(1, page_data.num_pages + 1), 'current_page': page})

    return HttpResponse(template.render(context))

    # return render(request, 'post_list.html',{'hello_world_arg':'JHJR1'} )
