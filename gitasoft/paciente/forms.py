'''
Created on 24/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.ext.db import djangoforms

from gitasoft.paciente import models as gm

class PacienteForm(djangoforms.ModelForm):
    class Meta:
        model = gm.Paciente
        exclude = ['user']

    def save(self, user, commit = True):
        post = super(PacienteForm, self).save(commit = False)
        post.user = user
        if commit:
            post.save()
        return post
