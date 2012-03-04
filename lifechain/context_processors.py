import simplejson
from social_auth.models import UserSocialAuth

def lifechain_context(request):
    context = {}
    lifechain_context = {}
    auths = UserSocialAuth.objects.filter(user = request.user, provider = "facebook")
    if len(auths) > 0:
        try:
            lifechain_context["facebook_id"] = auths[0].uid
            access_token = simplejson.loads(auths[0].extra_data)["access_token"]
            lifechain_context["facebook_access_token"] = simplejson.dumps(access_token)
        except:
            pass
    lifechain_context["loggedin"] = request.user.is_authenticated()
    lifechain_context["user"] = str(request.user)

    context["lifechain_context"] = simplejson.dumps(lifechain_context)
    return context
