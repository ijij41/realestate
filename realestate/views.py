# from django.shortcuts import render
#
# # Create your classviews here.
# from django.classviews.generic import TemplateView
#

import json

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
def get_search(request, page_num):
    result_as_json = get_search_result(request,page_num)
    return JsonResponse(result_as_json) #in case of coverting query set to json




########################################################################

#private function


def get_search_result(request, page_num):


    # print request.is_ajax()
    # print request.method
    # print request.body

    # note_form = SearchForm(request.POST)
    # print note_form

    # print request.body.decode('utf-8')
    print type(request)
    #
    print request.__dict__
    print type(request)
    print type(request.body)
    print request
    print "POST:", request.POST
    print "GET:", request.GET
    print "body:", request.body

    print "POst request value",     request.POST['userid']


    # print request.GET['title']

    # print simplejson.loads(request.body)
    # print request.POST['data']

    # serializers.deserialize("json",request.body))

    # JSONParser().parse(request)
    # ssss = json.loads(request.body)
    # print ssss

    # json_data = json.loads(request.body)
    # print json_data
    # print json_data['content']

    post_list = Deal.objects.all()
    num_content_per_page = 10
    paginator = Paginator(post_list, num_content_per_page)
    cur_page = page_num

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

    # data = serializers.serialize("json", post_list)
    data = serializers.serialize("json", contacts.object_list)
    dict_data = json.loads(data)
    return {"recordsTotal": 57, "recordsFiltered": 57, 'data':dict_data}





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

