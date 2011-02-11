# -*- encoding: utf-8 -*-
'''
Created on 25/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.ext import db

GITASOFT_TEMA = {'DEFAULT' : 'Padrão', 'AZUL' : 'Azul', 'VERDE' : 'Verde'}

TIPO_ATRIBUTO_EXTRA = (
    ('Phone', 'Phone'),
    ('Fax', 'Fax'),
    ('Email', 'Email'),
    ('AIM', 'AIM'),
    ('Gtalk', 'Gtalk/Jabber'),
    ('Yahoo', 'Yahoo'),
)

class Configuracao(db.Model):
    user = db.UserProperty()
    tema = db.StringProperty(choices = GITASOFT_TEMA)
    consultorio = db.StringProperty(verbose_name="Nome do consultório")
    responsavel = db.StringProperty(verbose_name="Responsável")
    reply_to = db.EmailProperty(verbose_name="E-mail para contato")
    
class AtributoExtra(db.Model):
    configuracao = db.ReferenceProperty(Configuracao)
    nome = db.StringProperty()
    descricao = db.StringProperty(verbose_name="Descrição")
    tipo = db.StringProperty(choices = TIPO_ATRIBUTO_EXTRA)
    entidade = db.StringProperty(required=True)
