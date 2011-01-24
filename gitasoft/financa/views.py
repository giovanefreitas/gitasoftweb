'''
Created on 12/01/2011

@author: giovanefreitas@gmail.com
'''
from google.appengine.ext import db
from django.shortcuts import render_to_response
from django.template import RequestContext
from gitasoft.financa import forms

import os
import django
from django import http
from django import shortcuts
from google.appengine.api import users

def respond(request, user, template, params=None):
    """Helper to render a response, passing standard stuff to the response.

    Args:
        request: The request object.
        user: The User object representing the current user; or None if nobody
            is logged in.
        template: The template name; '.html' is appended automatically.
        params: A dict giving the template parameters; modified in-place.

    Returns:
        Whatever render_to_response(template, params) returns.

    Raises:
        Whatever render_to_response(template, params) raises.
    """
    if params is None:
        params = {}
    if user:
        params['user'] = user
        params['sign_out'] = users.CreateLogoutURL('/')
        params['is_admin'] = (users.IsCurrentUserAdmin() and
                                                    'Dev' in os.getenv('SERVER_SOFTWARE'))
    else:
        params['sign_in'] = users.CreateLoginURL(request.path)
    if not template.endswith('.html'):
        template += '.html'
    return shortcuts.render_to_response(template, params)

def banco(request):
    user = users.GetCurrentUser()
    bancos = db.GqlQuery('SELECT * FROM Banco')
    return respond(request, user, 'financa/banco', {'bancos': bancos})

def conta_bancaria(request):
    form = forms.ContaBancariaForm()
    if request.method == 'POST':
        form = forms.ContaBancariaForm(request.POST)
        if form.is_valid():
            form.save(users.get_current_user())
            form = forms.ContaBancariaForm()
    
    user = users.get_current_user()
    contas = db.GqlQuery('SELECT * FROM ContaBancaria')
    return respond(request, user, 'financa/conta_bancaria', {'contas': contas, 'form': form})

def caixa(request):
    form = forms.MovimentacaoForm()
    if request.method == 'POST':
        form = forms.MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save(users.get_current_user())
    
    user = users.get_current_user()
    movimentacoes = db.GqlQuery('SELECT * FROM Movimentacao')
    return respond(request, user, 'financa/caixa', {'movimentacoes': movimentacoes, 'form': form})
