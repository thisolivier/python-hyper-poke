from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^view', views.show_all),
    url(r'^attack/(?P<victim_id>\d+)', views.do_poke)
]
