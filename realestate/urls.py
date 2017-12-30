
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout, password_change, password_change_done

from realestate import views
from realestate.classviews.templateTestView import TemplateTestView
from realestate.classviews.userCreationView import UserCreateView
from realestate.classviews.searchFormView import SearchFormView

from realestate.classviews.searchFormView import SearchFormView1





from django.views.generic import TemplateView

from realestate.views import LV

urlpatterns = [

    # unit tests #####################################################################################
    # template views
    #url(r'^template_test/$', TemplateTestView.as_view(), name="index_template_test"),  #reference
    url(r'^template_test/$', TemplateView.as_view(template_name='pages/blank.html'), name="test"),
    url(r'^template_typography/$', TemplateView.as_view(template_name='pages/typography.html'), name="topography"),
    url(r'^template_index/$', TemplateView.as_view(template_name='pages/index-ref.html'), name="index-ref"),
    url(r'^template_tables/$', TemplateView.as_view(template_name='pages/tables-ref.html'), name="table"),
    url(r'^template_icons/$', TemplateView.as_view(template_name='pages/icons.html'), name="icons"),
    url(r'^template_buttons/$', TemplateView.as_view(template_name='pages/buttons.html'), name="buttons"),

    # functional views
    url(r'^db_test/$', views.init_db_test, name='index_db_test'),
    url(r'^store_db_test/$', views.store_data_db_test, name='store_db_test'),
    #################################################################################################

    ###
    # url(r'^$', views.index, name="index"),
    # url(r'^', include('django.contrib.auth.urls')),

    # LOGIN_URL = '/realestate/login/'
    # LOGIN_REDIRECT_URL = '/realestate/main/'
    # templates/registration/login.html
    # templates/registration/register.html


    #FYI in user_manager, currently, here is real
    url(r'^login/$', login, name="login"),
    # url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'login_form.html'},name='login'),  #reference
    url(r'^logout/$', logout, {'next_page': 'realestate/login', }, name='logout'),
    url(r'^password_change/$', password_change, {'post_change_redirect':'realestate:search'}, name='password_change'),

    # url(r'^password_change_done/$', password_change_done, name='password_change_done'),

    url(r'^register/$', UserCreateView.as_view() , name='register'),

    url(r'^main/$', TemplateView.as_view(template_name='pages/index.html'), name="main"),



    url(r'^search/$', SearchFormView.as_view(), name="search"),
# http://127.0.0.1:8000/realestate/detail/9079552
    url(r'^detail/(?P<bldg_cd>\d+)/$', views.detail, name="detail"),



    url(r'^ajax/get_search/$', views.get_search, name='get_search'),
    url(r'^lv/page(?P<page>[0-9]+)/$', LV.as_view(), name="search_page"),
    #http://stackoverflow.com/questions/16931901/django-combine-detailview-and-formview

    url(r'^ajax/get_address_do/(?P<query_id>\w+)/(?P<query_key>\d+)/$', views.get_address_do, name='get_address_do'),  #query id : type of query (si, gu, dont),   query_key: keyworld (codes)
    # url(r'^ajax/get_search/(?P<page_num>[0-9]+)/$', views.get_search, name='get_search'),


    # login test  #http://www.slideshare.net/DustinJunginSeoul/qna-blog-using-django-orm
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^signup_ok/$', TemplateTestView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),


    # url(r'^login/$', login, name='login_url'),
    # url(r'^logout/$', logout, {'next_page': '/realestate/login', }, name='logout_url'),
    # url(r'^session_confirm/$', views.session_confirm, name='session_confirm'),

    # # practical page
    # url(r'^basic_search/$', SearchView.as_view(), name='basic_search'),
    # url(r'^search_result/$', SearchResultView.as_view(), name='search_result'),

]

