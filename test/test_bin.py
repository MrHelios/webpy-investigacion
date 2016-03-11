from nose.tools import *
import urllib

from bin.run import *
from app.db import BaseDatos
from test_tools import CasoTest

class TestNavegacion(CasoTest):

    def test_home(self):
        request = app.request('/')
        self.assert_status_OK(request.status)
        todos = BaseDatos().todo_elemento_tabla('myweb.db', 'cliente')
        self.assert_es_pagina(request.data, unicode(render.index(todos)))

    def test_home_confirmar_info(self):
        request = app.request('/')
        todos = BaseDatos().todo_elemento_tabla('myweb.db', 'cliente')
        # Aca busco por nombre:
        for cliente in todos: self.assert_esta_data(cliente[1], request.data)

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

    def test_registrar_GET(self):
        request = app.request('/registrar')
        self.assert_status_OK(request.status)

        form = registrar_form()
        self.assert_es_pagina(request.data, unicode(render.registrar(form)))

    def test_registrar_POST_redireccion(self):
        db = web.database(dbn='sqlite', db='myweb.db')
        cant_clientes = BaseDatos().contar_cant_clientes(db.select('cliente'))

        usuario = {'usuario': 'naranja'}
        data = urllib.urlencode(usuario)
        request = app.request('/registrar', method='POST', data=data)

        incremento_cliente = BaseDatos().contar_cant_clientes(db.select('cliente'))
        assert incremento_cliente > cant_clientes, 'Se esperaba que %d fuese mayor que %d' % (incremento_cliente, cant_clientes)

        db.delete('cliente', where='id=' + str(incremento_cliente))

        self.assert_es_status('303 See Other', request.status)

class TestUsuario(CasoTest):
    pass

if __name__ == '__main__':
    import web
    db = web.database(dbn='sqlite',db='myweb.db')
    cliente = db.select('cliente')

    # TestDataBase().borrar_entrada_en_db()
    # TestDataBase().borrar_entrada_en_db()
