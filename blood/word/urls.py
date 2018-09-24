from django.conf.urls import include, url
from . import  views

urlpatterns = [
    url(r'^datepicker/$',views.datastore,name='datepicker'),
    url(r'^$', views.index.as_view(),name='index'),
    url(r'^subscribe/$', views.subscribe,name='subscribe'),
    url(r'^Sendmail/$', views.Sendmail.as_view(),name='Sendmail'),
]