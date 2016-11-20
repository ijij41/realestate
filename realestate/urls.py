from django.conf.urls import url
from django.contrib import admin

from realestate import views
from realestate.class_views import TemplateTestView

urlpatterns = [


    # testunits
    url(r'^template_test/$', TemplateTestView.as_view(), name="index_template_test"),
    url(r'^db_test/$', views.init_db_test, name='index_db_test'),
    url(r'^store_db_test/$', views.store_data_db_test, name='store_db_test'),



]

