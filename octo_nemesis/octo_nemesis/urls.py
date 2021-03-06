from django.conf.urls import patterns, include, url

from octo_nemesis.views import stateset_views 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('octo_nemesis.views.stateset_views',
    # Examples:
    # url(r'^$', 'octo_nemesis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('octo_nemesis.urls')),

    url(r'^statesets/$', stateset_views.StateSetList.as_view()),
    url(r'^statesets/(?P<pk>[0-9]+)/?$', stateset_views.StateSetDetail.as_view())
)

# urlpatterns += patterns('octo_nemesis.views.state',