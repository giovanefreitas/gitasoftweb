# -*- encoding: utf-8 -*-
'''
Created on 12/01/2011

@author: giovanefreitas@gmail.com
'''
from google.appengine.ext.db import djangoforms
from gitasoft.financa import models as gm
from gitasoft.ext.validation import isUnique
from django.newforms.util import ValidationError

class ContaBancariaForm(djangoforms.ModelForm):
    def clean_numero(self):
        if 'numero' in self.clean_data:
            value = self.clean_data['numero'].strip()
            if value:
                return isUnique(self, 'numero', value)
        raise ValidationError('Por favor informe o número da conta.')

    banco = djangoforms.ModelChoiceField(gm.Banco, gm.Banco.all().order("nome"))
    
    class Meta:
        model = gm.ContaBancaria
        exclude = ['user']

    def save(self, user, commit = True):
        conta_bancaria = super(ContaBancariaForm, self).save(commit = False)
        conta_bancaria.user = user
        if commit:
            conta_bancaria.save()
        return conta_bancaria

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
