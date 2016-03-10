from nose.tools import *

class CasoTest:

    def assert_status_OK(self, status):
        assert '200 OK' == status, 'Se esperaba un 200 y se obtuvo %s' % status

    def assert_es_status(self, status_esp, status):
        assert status_esp == status, 'Se esperaba un %s y se obtuvo %s' % (status_esp, status)

    def assert_esta_data(self, esta, pagina):
        assert esta in pagina, 'Se esperaba encontrar %s en %s' % (esta, pagina)

    def assert_es_pagina(self, esta, pagina):
        assert esta == pagina, 'Se esperaba encontrar %r en cambio %r' % (pagina, esta)
