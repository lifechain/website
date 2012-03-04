from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    if request.user.is_authenticated():
        return render_to_response("home.html", {}, RequestContext(request))
    else:
        return render_to_response("landing.html", {}, RequestContext(request))
