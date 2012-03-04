from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import tastypie.api
import donormatch.api
api = tastypie.api.Api(api_name='v1')
api.register(donormatch.api.UserResource())
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'donormatch.views.home', name='home'),

    # Django social auth https://github.com/omab/django-social-auth
    url(r'', include('social_auth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^logout$', 'django.contrib.auth.views.logout'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
)
