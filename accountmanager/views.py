try:
    import json
except ImportError:
    import simplejson as json

from django.http import HttpResponse

from l10n.urlresolvers import reverse
import jingo

def handle(request):
    amcd = {
        'sessionstatus_path': reverse('accountmanager.views.session_status'),
        'connect_path': reverse('users.views.login'),
        'connect_params_username': 'username',
        'connect_params_password': 'password',
        'disconnect_path': reverse('users.views.logout'),
        'register_path': reverse('users.views.register'),
        'register_type': 'username',
        'register_params_id': 'username',
        'register_params_secret': 'password'
    }
    response = jingo.render(request, 'accountmanager/amcd.json', amcd)
    response['Content-type'] = 'application/json'
    return response
