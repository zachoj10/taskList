from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tasks.views',
	url(r'^(?P<user_id>\d+)/$', 'index'),
	url(r'^(?P<user_id>\d+)/tasks/(?P<task_id>\d+)/$', 'detail')
)	
