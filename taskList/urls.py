from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^user/', include('tasks.task_urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.login_page'),
    url(r'^login/authenticate/$', 'auth.views.login_user'),
    url(r'^logout/$', 'auth.views.logout_user'),
)
