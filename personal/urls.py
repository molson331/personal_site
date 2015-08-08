from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import IndexView, EventView, ResumeView

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', IndexView.as_view(), name='index'),

	# Personal pages
    url(r'^personal/event$', EventView.as_view(), name='event'),
    url(r'^personal/resume$', ResumeView.as_view(), name='resume'),
)
