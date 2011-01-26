# -*- encoding: utf-8 -*-
'''
Created on 25/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.ext import db

GITASOFT_TEMA = {'DEFAULT' : 'Padrão', 'AZUL' : 'Azul', 'VERDE' : 'Verde'}

class Configuracao(db.Model):
    user = db.UserProperty()
    tema = db.StringProperty(choices = GITASOFT_TEMA)
    consultorio = db.StringProperty(verbose_name="Nome do consultório")
    responsavel = db.StringProperty(verbose_name="Responsável")
    reply_to = db.EmailProperty(verbose_name="E-mail para contato")