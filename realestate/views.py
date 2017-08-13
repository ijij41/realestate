# from django.shortcuts import render
#
# # Create your classviews here.
# from django.classviews.generic import TemplateView
#

import json

import datetime
import time

from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView


from realestate.models import Deal, Address



def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("realestate:main"))
    else:
        return HttpResponseRedirect(reverse("realestate:login"))



class LV(ListView):
    model = Deal
    template_name = "pages/search.html"
    paginate_by = 3



#########################################################################

#for ajax

def get_address_do(request, query_id, query_key):
	leads_as_json = get_address(query_id, query_key)
	return JsonResponse(leads_as_json)  # in case of using custom dic


@csrf_exempt
# def get_search(request, page_num):
def get_search(request):
    result_as_json = get_search_result(request)
    return JsonResponse(result_as_json) #in case of coverting query set to json


########################################################################

#private function

# def get_search_result(request, page_num):
def get_search_result(request):

    ########## for debug ##################
    # print request.is_ajax()
    # print request.method
    # print request.body

    # print type(request)
    #
    # print request.__dict__
    # print type(request)
    # print type(request.body)
    # print request
    # print "POST:", request.POST
    # print "GET:", request.GET
    # print "body:", request.body
    #
    # print "1POst request value",     request.POST['si_code']
    ########################################


    house_type = request.POST['house_type']
    deal_type = request.POST['deal_type']

    si_code = request.POST['si_code']
    gu_code = request.POST['gu_code']
    dong_code = request.POST['dong_code']


    start_year = int(request.POST['start_year'])
    start_quarter = int(request.POST['start_quarter'])
    end_year = int(request.POST['end_year'])
    end_quarter = int(request.POST['end_quarter'])



    # https: // datatables.net / manual / server - side  # Sent-parameters
    # for pagination
    table_data_para_start = int(request.POST['start'])
    table_data_para_length = int(request.POST['length'])
    cur_page = table_data_para_start/table_data_para_length + 1

    # 1 1  2 4  3 7  4 10
    # year_range = [start_year, end_year],
    # https: // stackoverflow.com / questions / 4668619 / django - database - query - how - to - filter - objects - by - date - range
    # post_list = Deal.objects.all().filter(house_type=house_type, deal_type=deal_type,
    #                                       # si_code = si_code, gu_code=gu_code, dong_code=dong_code,
    #                                       deal_date__gte=datetime.date(start_year, (start_quarter*3)-2, 1),deal_date__lte=datetime.date(end_year, (end_quarter*3)-1, 1))


    post_list = Deal.objects.all().filter(deal_date__gte=datetime.date(start_year, (start_quarter*3)-2, 1),deal_date__lte=datetime.date(end_year, (end_quarter*3)-1, 1))



    print "original entry count:", len(post_list)
    if(not house_type=='0'):
        post_list = post_list.filter(housetype=house_type)
        print "select house_type:", house_type, len(post_list)
    if(not deal_type=='0'):
        post_list = post_list.filter(dealtype=deal_type)
        print "select deal_type:", deal_type
    if(not si_code=='0'):
        post_list = post_list.filter(sidocode=si_code)
        print "select si_code:", si_code
    if (not gu_code == '0'):
        post_list = post_list.filter(guguncode=gu_code)
        print "select gu_code:", gu_code
    if (not dong_code == '0'):
        post_list = post_list.filter(dongcode=dong_code)
        print "select dong_code:", dong_code



    # print 'get:', post_list
    print "-----------------"
    print type(house_type),house_type
    print type(deal_type), deal_type
    print type(si_code),si_code
    print type(gu_code), gu_code
    print type(dong_code), dong_code
    print "-----------------"

    print "test1:", post_list[0].address.si_code
    print "test2:", post_list[0].address.si_name


    # num_content_per_page = 10
    num_content_per_page = table_data_para_length
    paginator = Paginator(post_list, num_content_per_page)
    # cur_page = page_num  # page_num from url does not be needed because we will use start, length parameter provided from tabledata


    try:
        contacts = paginator.page(cur_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
        cur_page = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    # general paginate
    # page_list = [1, 2, 3, 4, 5]
    # previous_page = 0
    # next_page = 6
    # context = {}
    # context['object_list'] = contacts
    # context['object_list'] = contacts.object_list
    #
    # context['page_list'] = page_list    #
    # context['previous_page'] = previous_page
    # context['next_page'] = next_page    #
    # context['current_page'] = int(cur_page)

    # case 1
    # test = {'data': [{'content':"aaa",'page_info':{'page_list':[1,2,3,4],'prev_page':0,'next_page':5,'cur_page':3}}] }
    # return JsonResponse(test)

    # case 2
    # data = serializers.serialize("json",contacts.object_list)
    # d = ast.literal_eval(data)
    # return HttpResponse(data,content_type='application/json')

    # case 3
    # data = serializers.serialize("json", contacts.object_list)
    # context['object_list'] = data
    # return JsonResponse(context)

    # case 4
    # data = serializers.serialize("json", contacts.object_list)
    # # context['data'] = data
    # # return JsonResponse(context)

    # About json http://pythonstudy.xyz/python/article/205-JSON-%EB%8D%B0%EC%9D%B4%ED%83%80

    # according to page request, send data  (e.g., 2 page reuqest, send page 2 data
    data = serializers.serialize("json", contacts.object_list)
    dict_data = json.loads(data)

    #update from forienkey
    for de, pl in zip(dict_data, post_list):
        de['fields']['address'] = pl.get_address

    #TODO recordsFiltered processing
    return {"recordsTotal": post_list.count(), "recordsFiltered": post_list.count(), 'data':dict_data}





def get_address(query_id, query_key):
    if (query_id == 'si'):
        data_list = Address.objects.all().values('si_code', 'si_name').distinct()
    elif (query_id == 'gu'):
        data_list = Address.objects.all().values('gu_code', 'gu_name').distinct().filter(
            gu_code__startswith=query_key)
    elif (query_id == 'dong'):
        data_list = Address.objects.all().values('dong_code', 'dong_name').distinct().filter(
            dong_code__startswith=query_key)

    # c = serializers.serialize('json',data_list,field=('si_code','si_name'))
    # print process_data_list

    # data_list = [ entry for entry in data_list ]  #default for json
    process_data_list = []
    for entry in data_list:
        t_dic = {}
        if (query_id == 'si'):
            t_dic['code'] = entry['si_code']
            t_dic['name'] = entry['si_name']
        elif (query_id == 'gu'):
            t_dic['code'] = entry['gu_code']
            t_dic['name'] = entry['gu_name']
        elif (query_id == 'dong'):
            t_dic['code'] = entry['dong_code']
            t_dic['name'] = entry['dong_name']
        process_data_list.append(t_dic)

    # process_data_list = serializers.serialize('json',process_data_list)
    # return {'data':data_list}
    return {'data': process_data_list}


#######################################################################
def init_db_test(request):
    # latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    ##print "xxx", len(latest_question_list)
    # context = {'latest_question_list': latest_question_list}
    # return render(request,'polls/index.html', context)
    # data_list = get_object_or_404(Test, dongcode='1168010300')
    # jdata_list = Test.objects.filter(dongcode='1168010300').order_by(id).first()
    # data_list = Test.objects.all().filter(dongcode='1168010300')[:5]
    data_list = Deal.objects.filter(dongcode=1168010300)[:7]
    print "data count: ", len(data_list)
    print "data count: ", data_list
    print "data count: ", data_list.count

    context = {'test_list': data_list}
    return render(request, 'realestate/ref_show_data.html', context)


def store_data_db_test(request):
    addr = Address(si_code=1, si_name='test', gu_code=2, gu_name="gu_test", dong_code=3, dong_name="dong_test")
    addr.save()
    print "store data db test"
    return render(request, 'realestate/db_insert_done.html')

#
# def signup(request):
#     if request.method == "POST":
#         userform = UserCreationForm(request.POST)
#         if userform.is_valid():
#             userform.save()
#             return HttpResponseRedirect(reverse("realestate:signup_ok"))
#
#     elif request.method == "GET":
#         userform = UserCreationForm()
#
#     return render(request, "registration/signup.html",{"userform":userform})


# def session_confirm(request):
#     print User.get_full_name()
#     return None

