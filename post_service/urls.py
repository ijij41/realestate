from django.conf.urls import url

from post_service import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),

]




