# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from booking import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^add_booking_time/$', views.add_booking_time, name='add_booking_time'),
                       url(r'^booking_today/$', views.booking_today, name='booking_today'),
                       url(r'^person/$', views.person, name='person'),
                       url(r'^person/(?P<person_last_name_slug>[\w\-]+)/$', views.person, name='person'),
                       url(r'^(?P<person_city>[\w\-]+)/$', views.booking_city, name='booking_city')


                       )