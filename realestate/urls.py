
from django.conf.urls import url
from django.contrib.auth.views import login, logout

from realestate import views
from realestate.classviews.templateTestView import TemplateTestView

urlpatterns = [

    # unit tests
    # template views
    url(r'^template_test/$', TemplateTestView.as_view(), name="index_template_test"),
    # functional views
    url(r'^db_test/$', views.init_db_test, name='index_db_test'),
    url(r'^store_db_test/$', views.store_data_db_test, name='store_db_test'),

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
