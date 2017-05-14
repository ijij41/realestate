# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import FormView

from django.shortcuts import render
from realestate.forms import SearchForm
from realestate.models import Deal

# reload(sys)
# sys.setdefaultencoding('utf-8')



# for paginate, https://docs.djangoproject.com/es/1.9/topics/pagination/
class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'pages/search.html'


    def form_valid(self, form):   # this function is call when post requests incomming

        post_list = Deal.objects.all()[:6]
        num_content_per_page = 2
        paginator = Paginator(post_list, num_content_per_page)
        page = self.request.GET.get('page')

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        # print post_list    TODO delete
        # print type(post_list)
        # print post_list
        # # post_list.filter(housetype="A").update(housetype='아파트')
        # housetypeDict = {'A': 'APT', 'B': 'VILLA', 'C': 'HOUSE', 'E': 'OFFICETEL', 'F': 'DEAL_RIGHT', 'G': 'LAND'}

        context = {}
        context['form']=form
        context['object_list'] = contacts
        return render(self.request, self.template_name, context)


