import django
from django.conf.urls import url

from realestate.classviews.templateTestView import TemplateTestView
from user_manager import views

urlpatterns = [
    # custom
    # url(r'^login/$', views.login, name="login"),
    # url(r'^logout/$', views.logout, name="logout"),
    # url(r'^login/validate/$', views.login_validate, name="login_validate"),


    # signup
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signup_ok/$', TemplateTestView.as_view(template_name='signup_ok.html'), name='signup_ok'),


    # auth
    #url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'login_form.html'}, name='login'),
    #url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/user/login', }, name='logout'),

]
