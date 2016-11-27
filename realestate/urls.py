from django.conf.urls import url

from realestate import views
from realestate.classviews.templateTestView import TemplateTestView

urlpatterns = {

    # unit tests
    # template views
    url(r'^template_test/$', TemplateTestView.as_view(), name="index_template_test"),
    # functional views
    url(r'^db_test/$', views.init_db_test, name='index_db_test'),
    url(r'^store_db_test/$', views.store_data_db_test, name='store_db_test'),



    # # practical page
    # url(r'^basic_search/$', SearchView.as_view(), name='basic_search'),
    # url(r'^search_result/$', SearchResultView.as_view(), name='search_result'),

}

