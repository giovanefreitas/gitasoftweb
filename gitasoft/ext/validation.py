# -*- encoding: utf-8 -*-
'''
Created on 20/01/2011

@author: giovane
'''
from google.appengine.ext.db import djangoforms
from django.newforms.util import ValidationError

def isUnique(form, field, data):
    """Validates that a value is unique for a field.
    """
    if not isinstance(form, djangoforms.ModelForm):
        raise TypeError, u'The instance passed to isUnique is not a subclass of djangoforms.ModelForm'

    model = form._meta.model
    matching_obj = model.gql("WHERE " + field + " = :1", data).get()
    if not matching_obj:
        return data

    if form.instance and form.instance.key() == matching_obj.key():
        return data
    
    raise ValidationError(u'Já existe um %(optname)s com este %(fieldname)s.' % {'optname':model.kind(), 'fieldname':field})