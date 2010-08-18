try:
    import json
except ImportError:
    import simplejson as json

from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

def amcd(request):
    config = settings.AMCD_CONFIG
    params = {
        'status_path': reverse('accountmanager.views.status'),
        'connect_method': config['connect']['method'],
        'connect_path': reverse(config['connect']['path_view']),
        'connect_params_username': config['connect']['params']['username'],
        'connect_params_password': config['connect']['params']['password'],
        'disconnect_method': config['disconnect']['method'],
        'disconnect_path': reverse(config['disconnect']['path_view'])
    }
    return render_to_response('accountmanager/amcd.json', params,
                              mimetype='application/json')

def status(request):
    return HttpResponse()
