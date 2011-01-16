'''
Created on 15/01/2011

@author: giovane
'''
import sys
import os

# Remove the standard version of Django.
for k in [k for k in sys.modules if k.startswith('django')]:
  del sys.modules[k]

sys.path.append( os.path.join(os.path.dirname(__file__), '..' ) )

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

# Must set this env var before importing any part of Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import logging
import django.core.signals
import django.db
import django.dispatch.dispatcher

def log_exception(*args, **kwds):
  logging.exception('Exception in request:')

# Log errors.
django.dispatch.dispatcher.connect(
   log_exception, django.core.signals.got_request_exception)

# Unregister the rollback event handler.
django.dispatch.dispatcher.disconnect(
    django.db._rollback_on_exception,
    django.core.signals.got_request_exception)

from google.appengine.tools import bulkloader
from gitasoft.financa.models import * 

class BancoLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Banco',
                               [('codigo', str),
                                ('nome', str),
                                ('site', str)])
loaders = [BancoLoader]