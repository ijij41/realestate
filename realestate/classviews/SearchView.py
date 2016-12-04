import urllib

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from realestate.forms import SearchForm


class SearchView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'sbadmin/pages/search.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        # print request.POST['dong_code'], request.POST['your_name']




        if form.is_valid():
            # print "all values", form.__dict__
            deal_type = form.cleaned_data['deal_type']

            si_code = form.cleaned_data['si_code']
            gu_code = form.cleaned_data['gu_code']
            dong_code = form.cleaned_data['dong_code']

            start_year = form.cleaned_data['start_year']
            start_quarter = form.cleaned_data['start_quarter']
            end_year = form.cleaned_data['end_year']
            end_quarter = form.cleaned_data['end_quarter']

            print request.POST['si_code'], request.POST['gu_code']
            # new_name = form.cleaned_data['your_name']
            # print "PASS:is_valid:", dong_code, new_name
            # redirect_str = reverse('mysql_test:search_result', kwargs={'page_list': 11} )

            redirect_str = reverse('mysql_test:search_result')
            dict_tmp = form.cleaned_data
            # dict_tmp['page']=1
            final_url = "%s?%s" % (redirect_str, urllib.urlencode(form.cleaned_data))
            # final_url = "%s?%s" % (redirect_str, urllib.urlencode(dict_tmp))
            return HttpResponseRedirect(final_url)

        return render(request, 'sbadmin/pages/search.html', {'form': form})
