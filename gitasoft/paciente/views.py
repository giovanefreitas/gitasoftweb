'''
Created on 24/01/2011

@author: giovanefreitas@gmail.com
'''
from google.appengine.api import users
from gitasoft.ext import template_util as utils
from gitasoft.paciente import models as gm
from gitasoft.paciente import forms

def paciente(request):
    form = forms.PacienteForm()
    if request.method == 'POST':
        paciente = gm.Paciente()
        paciente.nome = request.POST['nome']
        atributos_extras = request.POST.iteritems()
        for k, v in atributos_extras:
            if paciente.properties().get(k) == None:
                setattr(paciente, k, v)
        paciente.user = users.get_current_user()
        paciente.put()
    
    user = users.get_current_user()
    params = {'pacientes': gm.Paciente.all(), 'form': form}
    return utils.respond(request, user, 'paciente/ficha', params)