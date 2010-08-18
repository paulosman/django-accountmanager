from setuptools import setup

setup(
    name='accountmanager',
    version='0.1dev',
    install_requires=['wellknown'],
    packages=['accountmanager'],
    dependency_links=[
        'http://code.eval.ca/python/releases/django-wellknown',
    ],
)
