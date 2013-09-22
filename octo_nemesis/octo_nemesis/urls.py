from django.conf.urls import patterns, include, url

from octo_nemesis.views import stateset 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('octo_nemesis.views.stateset',
    # Examples:
    # url(r'^$', 'octo_nemesis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('octo_nemesis.urls')),
    
    url(r'^stateset/$', 'stateset_list'),
    url(r'^stateset/(?P<pk>[0-9]+)/$', 'stateset_detail')
)

# urlpatterns += patterns('octo_nemesis.views.state',