'''
Created on 12/01/2011

@author: giovanefreitas@gmail.com
'''
from google.appengine.ext.db import djangoforms
from gitasoft.financa import models as gm

class ContaBancariaForm(djangoforms.ModelForm):
    class Meta:
        model = gm.ContaBancaria
        exclude = ['user']

    def save(self, user, commit = True):
        post = super(ContaBancariaForm, self).save(commit = False)
        post.user = user
        if commit:
            post.save()
        return post

class MovimentacaoForm(djangoforms.ModelForm):
    class Meta:
        model = gm.Movimentacao
        exclude = ['user']

    def save(self, user, commit = True):
        post = super(MovimentacaoForm, self).save(commit = False)
        post.user = user
        if commit:
            post.save()
        return post
