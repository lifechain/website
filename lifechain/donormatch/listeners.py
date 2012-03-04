from social_auth.signals import pre_update
from social_auth.backends.facebook import FacebookBackend
from donormatch.models import UserProfile
import datetime

def facebook_extra_values(sender, user, response, details, **kwargs):
    try:
        # Load an existing user profile if we have one
        userprofile = UserProfile.objects.get(user = user)
    except:
        # Must be a new user, create one
        userprofile = UserProfile(user = user)

    print response.get("birthday")
    try:
        birthday = datetime.datetime.strptime(response.get("birthday"), '%m/%d/%Y')
        userprofile.birthday = birthday
    except:
        # Something wrong with date format. Ignore
        pass
    userprofile.location = response.get("location", {}).get("name")
    userprofile.lattitude = 0
    userprofile.longitude = 0

    if response.get("gender") == "male":
        userprofile.sex = 'm'
    elif response.get("gender") == "female":
        userprofile.sex = 'f'

    userprofile.save()

    return True

pre_update.connect(facebook_extra_values, sender=FacebookBackend)
