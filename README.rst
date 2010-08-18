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

Optionally specify a path to the account manager control document by setting ``MOZILLA_AMCD_HREF`` in ``settings.py``: ::

     MOZILLA_AMCD_HREF = '/meta/amcd.json'

Configure ``urls.py`` in your project: ::

     (r'^meta/amcd.json$', include('accountmanager.views.handle'))
