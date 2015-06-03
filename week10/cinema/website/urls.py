from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('website.views', url(r'^$', 'home'))
