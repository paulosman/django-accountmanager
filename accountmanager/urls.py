from django.conf.urls.defaults import *

urlpatterns = patterns('',
  (r'^meta/amcd.json$',  'accountmanager.views.handle'),
)
