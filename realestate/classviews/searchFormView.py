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

        post_list = Deal.objects.all()
        num_content_per_page = 5
        paginator = Paginator(post_list, num_content_per_page)
        cur_page = self.request.GET.get('page')

        try:
            contacts = paginator.page(cur_page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
            cur_page = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)


        page_list=[1,2,3,4,5]
        previous_page = 0
        next_page = 6

        context = {}
        context['form']=form
        context['object_list'] = contacts
        context['page_list'] = page_list
        context['previous_page']=previous_page
        context['next_page'] = next_page
        context['current_page'] = int(cur_page)

        # page_index = int(page) % num_content_per_page
        # previous_page = int(page) / num_content_per_page
        # last_page = len(post_list) / num_content_per_page + 1
        # context['page_index'] = page_index
        #
        # context['num_content_per_page'] = num_content_per_page
        # context['previous_page'] = previous_page
        # context['last_page']=last_page
        # context['paginator'] = paginator

        return render(self.request, self.template_name, context)


