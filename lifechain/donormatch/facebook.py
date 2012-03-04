from donormatch.models import UserProfile
from social_auth.signals import pre_update
from social_auth.backends.facebook import FacebookBackend, FACEBOOK_ME
from urllib2 import urlopen
from urllib import urlencode
import datetime
import simplejson

def fetch_facebook_friends(user, response):
    access_token = response['access_token']
    url = FACEBOOK_ME.rstrip('?') + '/friends?' + urlencode({'access_token': access_token})
    print url
    try:
        data = simplejson.load(urlopen(url))
    except ValueError:
        print 'Could not load friend list from Facebook.'
        data = {}
    return data



def facebook_extra_values(sender, user, response, details, **kwargs):
    try:
        # Load an existing user profile if we have one
        userprofile = UserProfile.objects.get(user = user)
    except:
        # Must be a new user, create one
        userprofile = UserProfile(user = user)

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

    facebook_friends = fetch_facebook_friends(user, response)
    userprofile.facebook_friends = simplejson.dumps(facebook_friends["data"])

    userprofile.save()

    return True

pre_update.connect(facebook_extra_values, sender=FacebookBackend)


