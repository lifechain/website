from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import tastypie.api
import donormatch.api
api = tastypie.api.Api(api_name='v1')
api.register(donormatch.api.UserProfileResource())
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'donormatch.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
)
