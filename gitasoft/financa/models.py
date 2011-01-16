# -*- encoding: utf-8 -*-
'''
Created on 12/01/2011

@author: giovanefreitas@gmail.com
'''
from google.appengine.ext import db
from gitasoft.ext.money import MoneyProperty

class Banco(db.Model):
    codigo = db.StringProperty(verbose_name='Código')
    nome = db.StringProperty()
    site = db.StringProperty()

class ContaBancaria(db.Model):
    banco = db.ReferenceProperty(Banco)
    agencia = db.StringProperty(verbose_name='Agência')
    numero = db.StringProperty(verbose_name='Número')
    descricao = db.StringProperty(verbose_name='Descrição')
    user = db.UserProperty(required=True)

class Movimentacao(db.Model):
    data = db.DateTimeProperty(auto_now_add = True)
    descricao = db.StringProperty(verbose_name='Descrição')
    valor = MoneyProperty(required=True)
    conta_bancaria = db.ReferenceProperty(ContaBancaria, verbose_name='Conta bancária')
    user = db.UserProperty(required=True)

