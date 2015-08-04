from django.conf.urls import patterns, include, url

from views import EventView, ResumeView

urlpatterns = patterns('',
    url(r'^event$', EventView.as_view(), name='event'),
    url(r'^resume$', ResumeView.as_view(), name='resume'),
)
