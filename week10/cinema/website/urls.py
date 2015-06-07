from django.conf.urls import url, patterns


urlpatterns = patterns('website.views',
    url(r'^$', 'index'),
    url(r'reserved/$', 'reserved'),
    url(r'register/$', 'register'),
    # url(r'reservation/$', 'reservation', name='reservation'),
    url(r'reservation/(?P<projection_id>[0-9]+)/$', 'reservation', name='reservation'),
)
