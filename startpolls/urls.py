from django.conf.urls import url
from django.contrib import admin

from startpolls.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(),name="indexto"),
]
