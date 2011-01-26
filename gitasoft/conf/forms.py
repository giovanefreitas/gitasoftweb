'''
Created on 25/01/2011

@author: giovanefreitas@gmail.com
'''

from google.appengine.ext.db import djangoforms

from gitasoft.conf import models as gm

class ConfiguracaoForm(djangoforms.ModelForm):
    class Meta:
        model = gm.Configuracao
        exclude = ['user']

    def save(self, user, commit = True):
        post = super(ConfiguracaoForm, self).save(commit = False)
        post.user = user
        if commit:
            post.save()
        return post
