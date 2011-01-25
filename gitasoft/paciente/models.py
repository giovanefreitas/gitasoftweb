'''
Created on 24/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.ext import db

class Paciente(db.Expando):
    nome = db.StringProperty()
    user = db.UserProperty()