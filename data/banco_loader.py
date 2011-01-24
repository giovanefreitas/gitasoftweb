'''
Created on 15/01/2011

@author: giovane
'''
import os
import sys

sys.path.append( os.path.join(os.path.dirname(__file__), '..' ) )

from google.appengine.tools import bulkloader
from gitasoft.financa.models import * 


def convert_failure(value):
    if value is None:
        return value
    else:
        return value.decode('utf-8')

class BancoLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Banco',
                               [('codigo', str),
                                ('nome', convert_failure),
                                ('site', convert_failure)])
loaders = [BancoLoader]