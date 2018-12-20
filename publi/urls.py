from django.urls import re_path

from . import views

app_name = "publi"
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^labo/$', views.labo, name='labo'),
    re_path(r'^rv/$', views.rv, name='rv'),
    re_path(r'^comhet/$', views.comhet, name='comhet'),
    re_path(r'^geomecanique/$', views.geomecanique, name='geomecanique'),
    ]
