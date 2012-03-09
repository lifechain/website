import os, sys
sys.path.append('/home/ubuntu/lifechainenv/lib/python2.7/site-packages')
sys.path.append('/home/ubuntu/src/lifechain')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lifechain.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
