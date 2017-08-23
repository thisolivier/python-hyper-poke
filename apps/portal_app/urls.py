from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^register', views.process_reg),
    url(r'^login', views.process_login),
    url(r'^logout', views.logout),
    url(r'^', views.display_forms),
]
