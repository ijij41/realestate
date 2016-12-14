from django.conf.urls import url

from user_manager import views

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^login/validate/$', views.login_validate, name="login_validate"),
]
