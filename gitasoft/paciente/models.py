# -*- encoding: utf-8 -*-
'''
Created on 24/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.ext import db

class Paciente(db.Expando):
    nome = db.StringProperty()
    user = db.UserProperty()

    #nome gravado em forma de pronúncia, 
    #para apresentar como resultados extras na seção "Você quis dizer..."
    nome_fonema = db.StringProperty() 