# Copyright 2008 Google Inc.
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


from django.conf.urls.defaults import *

#handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns(
    '',
    (r'^$', 'views.index'),
    (r'^new$', 'views.new'),
    (r'^edit/(\d+)$', 'views.edit'),

    #Modulo financeiro
    ('^fin/banco/$', 'gitasoft.financa.views.banco'),
    ('^fin/banco/conta/$', 'gitasoft.financa.views.conta_bancaria'),
    ('^fin/caixa/$', 'gitasoft.financa.views.caixa'),
    
    #Modulo de pacientes
    ('^paciente/$', 'gitasoft.paciente.views.paciente'),
    
    )