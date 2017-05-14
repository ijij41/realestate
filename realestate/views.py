# from django.shortcuts import render
#
# # Create your classviews here.
# from django.classviews.generic import TemplateView
#
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
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
	return JsonResponse(leads_as_json)




########################################################################

#private function


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