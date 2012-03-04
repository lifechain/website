import simplejson
from social_auth.models import UserSocialAuth

def lifechain_context(request):
    context = {}
    lifechain_context = {}
    if request.user.is_authenticated():
        auths = UserSocialAuth.objects.filter(user = request.user, provider = "facebook")
        if len(auths) > 0:
            lifechain_context["facebook_id"] = auths[0].uid
            access_token = auths[0].extra_data["access_token"]
            lifechain_context["facebook_access_token"] = access_token

    lifechain_context["loggedin"] = request.user.is_authenticated()
    lifechain_context["username"] = str(request.user)
    # lifechain_context["first_name"] = str(request.user.first_name)
    # lifechain_context["last_name"] = str(request.user.last_name)
    # lifechain_context["email"] = str(request.user.email)
    # lifechain_context["birthday_date"] = str(request.user.userprofile.birthday)
    # #lifechain_context["facebook_friends"] = str(request.user.userprofile.facebook_friends)
    # lifechain_context["lattitude"] = str(request.user.userprofile.lattitude)
    # lifechain_context["longitude"] = str(request.user.userprofile.longitude)
    # lifechain_context["location"] = str(request.user.userprofile.location)
    # lifechain_context["phone"] = str(request.user.userprofile.phone)
    # lifechain_context["sex"] = str(request.user.userprofile.sex)

    context["lifechain_context"] = simplejson.dumps(lifechain_context, indent=1)
    return context
