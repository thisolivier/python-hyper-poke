from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^register', views.process_reg),
    url(r'^login', views.process_login),
    url(r'^logout', views.process_logout),
    url(r'^confirmation', views.display_delete),
    url(r'^delete', views.process_delete),
    url(r'^', views.display_login)
]
