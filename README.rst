=====================
django-accountmanager
=====================

Django application that provides drop-in support for the `Mozilla Account Manager`_ addon. It's not quite usable yet. Stay tuned.

.. _Mozilla Account Manager: http://mozillalabs.com/blog/2010/03/account-manager/

Requirements
------------

In order to use ``django-accountmanager``, you will need to install: 

     * Django 
     * `django-wellknown`_

.. _django-wellknown: http://github.com/paulosman/django-wellknown

Installation
------------

Install django-accountmanager from the git repository: ::

     pip install -e git://github.com/paulosman/django-accountmanager#egg=accountmanager

Add django-accountmanager to your ``INSTALLED_APPS`` in ``settings.py`` **after** ``wellknown``: ::

     INSTALLED_APPS = (
         ...
         'wellknown',
         ...
         'accountmanager',
         ...
     )

Add ``accountmanager.middleware.StatusHeader`` to ``MIDDLEWARE_CLASSES`` in ``settings.py``: ::

     MIDDLEWARE_CLASSES = (
        ...
        'accountmanager.middleware.StatusHeader',
        ...
     )

Configure ``urls.py`` in your project: ::

     urlpatterns = patterns('', 
         ...
     	 (r'^accountmanager/', include('accountmanager.urls'))
     )

Configure account manager control document settings in ``settings.py``: ::

     AMCD_CONFIG = {
         'connect': {
             'method': 'POST', 
             'path_view': 'users.views.login',
             'params': {
                 'username': 'username',
                 'password': 'password'
             }
         },
         'disconnect': {
             'method': 'GET',
             'path_view': 'users.views.logout'
         }
     }

Optionally specify custom ``reverse`` function in ``settings.py``: ::

    AMCD_RESOLVER_FUNCTION = 'l10n.urlresolvers.reverse'
