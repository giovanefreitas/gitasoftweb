'''
Created on 15/01/2011

@author: giovane
'''
from google.appengine.tools import bulkloader
from gitasoft.financa.models import * 

class BancoLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Banco',
                               [('codigo', str),
                                ('nome', str),
                                ('site', str)])
loaders = [BancoLoader]