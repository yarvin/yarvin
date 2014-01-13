from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yarvin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rsvp/', include('rsvp.urls', namespace="rsvp")),
    url(r'^admin/', include(admin.site.urls)),
)
