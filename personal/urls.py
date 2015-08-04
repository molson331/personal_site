from django.conf.urls import patterns, include, url

from views import EventView

urlpatterns = patterns('',
    url(r'^event$', EventView.as_view(), name='event'),
)
