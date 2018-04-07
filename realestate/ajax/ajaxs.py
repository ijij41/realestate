import datetime



import json
# from django.core.serializers import json  # dont use
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.http import JsonResponse

from django.db.models import F, Sum, Count, Case, When

from realestate.models import Deal, Address



def get_rent_rank(request):   ## main function for search
    result_as_json = get_search_result(request)
    print result_as_json
    return JsonResponse(result_as_json) #in case of coverting query set to json


def getStartTime(start_year, start_quarter):
    return datetime.date(start_year, (start_quarter * 3) - 2, 1)


def getEndTime(end_year, end_quarter):
    if ((((end_quarter + 1) * 3) - 2) > 12):
        end_time = datetime.date(end_year + 1, 1, 1)
    else:
        end_time = datetime.date(end_year, ((end_quarter + 1) * 3) - 2, 1)
    # print "end date:", end_time
    return end_time

def getPaginateInfo(start,length):
    cur_page = start/length + 1
    size_per_page = length
    return cur_page, size_per_page



def get_search_result(request):

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




    cur_page, size_per_page = getPaginateInfo(table_data_para_start,table_data_para_length)
    start_time = getStartTime(start_year, start_quarter)
    end_time = getEndTime(end_year, end_quarter)
    # print cur_page, size_per_page, start_time, end_time




    post_list = Deal.objects.filter(deal_date__gte=start_time, deal_date__lt=end_time, )
    if(not house_type=='0'):
        post_list = post_list.filter(housetype=house_type)
    if(not deal_type=='0'):
        post_list = post_list.filter(dealtype=deal_type)


    # if(not si_code=='0'):
    #     post_list = post_list.filter(sidocode=si_code)
    #     print "select si_code:", si_code, len(post_list)
    # if (not gu_code == '0'):
    #     post_list = post_list.filter(guguncode=gu_code)
    #     print "select gu_code:", gu_code, len(post_list)
    # if (not dong_code == '0'):
    #     post_list = post_list.filter(dongcode=dong_code)
    #     print "select dong_code:", dong_code, len(post_list)

    print post_list.values('bldg_cd','bldg_nm').annotate(count_num=Count('bldg_cd')).order_by('-count_num')



    paginator = Paginator(post_list, size_per_page)
    try:
        contacts = paginator.page(cur_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
        cur_page = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    tmp_data = serializers.serialize("json", contacts.object_list)
    return_data = json.loads(tmp_data)  # return data to web. In addition, in case of address (forien key), manually update from deal to real return data(json)
    #post_list is data used in here (django.py
    #update from forienkey
    for de, pl in zip(return_data, post_list):
        de['fields']['address'] = pl.get_address


    #TODO recordsFiltered processing
    return {"recordsTotal": post_list.count(), "recordsFiltered": post_list.count(), 'data':return_data}
