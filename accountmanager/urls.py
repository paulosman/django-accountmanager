from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^amcd.json$',    'accountmanager.views.amcd'),
    (r'^status$',       'accountmanager.views.status'),
)
