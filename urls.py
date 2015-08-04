from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from personal.views import IndexView

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', IndexView.as_view(), name='index'),

	# Personal pages
	url(r'^personal/', include('personal.urls')),
)
