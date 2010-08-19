try:
    import json
except ImportError:
    import simplejson as json

from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

def _get_url_resolver(resolver):
    """
    Extract callable function from the string ``resolver`` which is a
    function name, optionally prefixed with a package name. If no callable
    function can be found, return ``django.core.urlresolvers.reverse``.
    """
    if resolver in globals():
        return globals()[resolver]
    
    if '.' in resolver:
        parts = resolver.split('.')
        try:
            m = __import__(parts[0])
        except ImportError:
            return reverse 
        for part in parts[1:]:
            resolver = getattr(m, part)
            if not callable(resolver):
                m = resolver
        return resolver

    return reverse

def amcd(request):
    """Serve the account manager control document."""
    config = settings.AMCD_CONFIG
    resolver = getattr(settings, 'AMCD_RESOLVER_FUNCTION', reverse)
    if not callable(resolver):
        resolver = _get_url_resolver(resolver)
    params = {
        'status_path': resolver('accountmanager.views.status'),
        'connect_method': config['connect']['method'],
        'connect_path': resolver(config['connect']['path_view']),
        'connect_params_username': config['connect']['params']['username'],
        'connect_params_password': config['connect']['params']['password'],
        'disconnect_method': config['disconnect']['method'],
        'disconnect_path': resolver(config['disconnect']['path_view']),
        'register_method': config['register']['method'],
        'register_path': resolver(config['register']['path_view']),
        'register_type': config['register']['type'],
        'register_params_id': config['register']['params']['id'],
        'register_params_secret': config['register']['params']['secret'],
    }
    return render_to_response('accountmanager/amcd.json', params,
                              mimetype='application/json')

def status(request):
    """Just serve headers and an empty 200 OK response."""
    return HttpResponse()
