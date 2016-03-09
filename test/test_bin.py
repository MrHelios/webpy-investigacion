from nose.tools import *
from bin.run import *
import urllib

from test_tools import CasoTest

class TestNavegacion(CasoTest):

    def test_home(self):
        request = app.request('/')
        self.assert_status_OK(request.status)
        self.assert_es_pagina(request.data, unicode(render.index()))

    def test_form_GET(self):
        request = app.request('/form')
        self.assert_status_OK(request.status)
        self.assert_es_pagina(request.data, unicode(render.form()))

    def test_form_POST(self):
        nombre = {'dato': 'Viva la senior'}
        data = urllib.urlencode(nombre)
        request = app.request('/form', method='POST', data=data)
        self.assert_status_OK(request.status)
        resp = 'Viva la senior'
        self.assert_es_pagina(request.data, resp)
