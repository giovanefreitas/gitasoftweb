'''
Created on 25/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.ext.db import djangoforms
from google.appengine.ext import db

from gitasoft.conf import models as gm

class ConfiguracaoForm(djangoforms.ModelForm):
    class Meta:
        model = gm.Configuracao
        exclude = ['user']

    def save(self, user, commit=True):
        post = super(ConfiguracaoForm, self).save(commit=False)
        post.user = user
        if commit:
            post.save()
        return post
    
    def atributos_paciente(self):
        for name, value in self.data.items():
            if name.startswith('atributo_paciente_'):
                id_atributo = self.data.get('id_' + name)
                atributo = gm.AtributoExtra.get(db.Key.from_path('AtributoExtra', id_atributo))
                if atributo:
                    atributo.nome = value
                else:
                    atributo = gm.AtributoExtra(nome=value, entidade='Paciente')
                
                yield (atributo)
