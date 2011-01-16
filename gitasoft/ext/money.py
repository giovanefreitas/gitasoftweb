#!/usr/bin/env python
#
# Copyright 2010 GitaSoft Desenvolvimento de Sistemas Ltda.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import db
 
class Money(object):
    multiple = 1000000.0
    def __init__(self, val, multiply=True):
        if multiply:
            self._intVal = int(float(val) * self.multiple)
        else:
            self._intVal = int(val)
 
    def format(self, places=2):
        return "%.*f" % (places, float(self))
 
    def __float__(self):
        return self._intVal / self.multiple
 
    def __repr__(self):
        return "%.06f" % (self._intVal / self.multiple)
 
    def __mul__(self, other):
        if type(other) == Money:
            return Money((self._intVal * other._intVal) / self.multiple, False)
        else:
            return Money(self._intVal * other, False)
 
    __rmul__ = __mul__
    def __add__(self, other):
        if type(other) == Money:
            return Money(self._intVal + other._intVal, False)
        else:
            return Money(self._intVal + (other * self.multiple), False)
 
    __radd__ = __add__
 
    def __cmp__(self, other):
        if other == None:
            return 1
        elif other == "":
            return 1
        elif type(other) != Money:
            return self._intVal - other * self.multiple
        return self._intVal - other._intVal
 
    def __sub__(self, other): 
        return Money(self._intVal - other._intVal, False)
 
    def __rsub__(self, other): 
        return Money(other._intVal - self._intVal, False)
 
    def __div__(self, other): 
        if type(other) == Money:
            return Money((self._intVal * self.multiple) / other._intVal, False)
        else:
            return Money(self._intVal / other, False)
 
    def __rdiv__(self, other): 
        if type(other) == Money:
            return Money((other._intVal * self.multiple) / self._intVal, False)
        else:
            return Money((other * self.multiple * self.multiple) / self._intVal, False)
 
    def __neg__(self): 
        return Money(self._intVal * -1, False)
 
class MoneyProperty(db.Property):
    data_type = Money
 
    def get_value_for_datastore(self, model_instance):
        value = super(MoneyProperty, self).get_value_for_datastore(model_instance)
        if value == None:
            return None
        elif isinstance(value, Money):
            return value._intVal
        else:
            return Money(value)._intVal
    def make_value_from_datastore(self, value):
        if value == None:
            return None
        else:
            return Money(value, False)
 
    def empty(self, value):
        return value == None
 
    def get_value_for_form(self, instance):
        value = super(MoneyProperty, self).get_value_for_form(instance)
        if not value:
            return None
        if isinstance(value, Money):
            return float(value)
        return value
 
    def make_value_from_form(self, value):
        if not value:
            return []
        if isinstance(value, Money):
            return Money(value)
        return value
