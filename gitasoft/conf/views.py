'''
Created on 25/01/2011

@author: giovanefreitas@gmail.com
'''
from google.appengine.api import users
from gitasoft.ext import template_util as utils
from gitasoft.conf import models as gm
from gitasoft.conf import forms

def conf(request):
    user = users.get_current_user()
    configuracao = gm.Configuracao.all().get()
    if configuracao == None:
        configuracao = gm.Configuracao(user=user)
    form = forms.ConfiguracaoForm(instance=configuracao)
    
    if request.method == 'POST':
        form = forms.ConfiguracaoForm(request.POST, instance=configuracao)
        if form.is_valid():
            form.save(user)
            for (atributo) in form.atributos_paciente():
                atributo.put()
    
    params = {
        'form': form, 
        'perfis' : gm.Configuracao.all(),
        'atributos_paciente' : gm.AtributoExtra.gql("WHERE entidade = 'Paciente' "),
    }
    
    return utils.respond(request, user, 'conf/conf.html', params)