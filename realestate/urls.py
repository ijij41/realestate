from django.conf.urls import url
from django.contrib import admin

from realestate.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(),name="indexto"),
]
