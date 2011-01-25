'''
Created on 12/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.api import users

from gitasoft.ext import template_util as utils
from gitasoft.financa import forms
from gitasoft.financa import models as gm

def banco(request):
    user = users.GetCurrentUser()
    params = {'bancos': gm.Banco.all()}
    return utils.respond(request, user, 'financa/banco', params)

def conta_bancaria(request):
    form = forms.ContaBancariaForm()
    if request.method == 'POST':
        form = forms.ContaBancariaForm(request.POST)
        if form.is_valid():
            form.save(users.get_current_user())
            form = forms.ContaBancariaForm()
    
    user = users.get_current_user()
    params = {'contas': gm.ContaBancaria.all(), 'form': form}
    return utils.respond(request, user, 'financa/conta_bancaria', params)

def caixa(request):
    form = forms.MovimentacaoForm()
    if request.method == 'POST':
        form = forms.MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save(users.get_current_user())
    
    user = users.get_current_user()
    params = {'movimentacoes': gm.Movimentacao.all(), 'form': form}
    return utils.respond(request, user, 'financa/caixa', params)
