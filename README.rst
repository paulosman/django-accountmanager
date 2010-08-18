=====================
django-accountmanager
=====================

Django application that provides drop-in support for the `Mozilla Account Manager`_ addon. It's not usable yet. Stay tuned.

.. _Mozilla Account Manager: http://mozillalabs.com/blog/2010/03/account-manager/

Installation
------------

Install django-accountmanager from the git repository: ::

     pip install -e git://github.com/paulosman/django-accountmanager#egg=accountmanager

Add django-accountmanager to your ``INSTALLED_APPS`` in ``settings.py``: ::

     INSTALLED_APPS = (
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
