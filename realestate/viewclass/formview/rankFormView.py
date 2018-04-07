# -*- coding: utf-8 -*-
from django.views.generic import FormView
from realestate.formclass.RankForm import RankForm


class RankFormView(FormView):

    form_class = RankForm   #set form
    template_name = 'pages/rank.html' #set view

    # this function will not be called because submit button in template called javascript to call ajax
    def form_valid(self, form):   # this function is call when post requests incomming
        print "This function is form valid but I will use javascript. So it's not called"
        pass

        # post_list = Deal.objects.all()
        # num_content_per_page = 5
        # paginator = Paginator(post_list, num_content_per_page)
        # cur_page = self.request.GET.get('page')
        #
        # try:
        #     contacts = paginator.page(cur_page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     contacts = paginator.page(1)
        #     cur_page = 1
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     contacts = paginator.page(paginator.num_pages)
        #
        #
        # page_list=[1,2,3,4,5]
        # previous_page = 0
        # next_page = 6
        #
        # context = {}
        # context['form']=form
        # context['object_list'] = contacts
        #
        # context['page_list'] = page_list
        #
        # context['previous_page']=previous_page
        # context['next_page'] = next_page
        #
        # context['current_page'] = int(cur_page)



        # return render(self.request, self.template_name, context)
