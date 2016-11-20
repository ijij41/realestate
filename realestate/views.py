# from django.shortcuts import render
#
# # Create your views here.
# from django.views.generic import TemplateView
#
from django.shortcuts import render

from realestate.models import Deal, Address


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
