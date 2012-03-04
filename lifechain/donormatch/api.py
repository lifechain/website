from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
import tastypie.fields

import donormatch.models

class SessionAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        return request.user.is_authenticated()
    
    def get_identifier(self, request):
        if request.user.is_authenticated():
            return request.user.username

class UserAuthorization(Authorization):
    def is_authorized(self, request, object=None):
        return request.user.is_authenticated()
    
    def apply_limits(self, request, object_list):
        if request and hasattr(request, 'user'):
            return object_list.filter(username=request.user.username)
        else:
            return object_list.none()

class UserResource(ModelResource):
    userprofile = tastypie.fields.ToOneField(donormatch.models.UserProfile, 'userprofile', full=True, null=True)
    class Meta:
        queryset = donormatch.models.User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = SessionAuthentication()
        authorization = UserAuthorization()

class UserLink(ModelResource):
    class Meta:
        queryset = donormatch.models.UserLink.objects.all()
        resource_name = 'userlink'
