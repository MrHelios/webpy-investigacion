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

    def test_registrar_GET(self):
        request = app.request('/registrar')
        self.assert_status_OK(request.status)

        form = registrar_form()
        self.assert_es_pagina(request.data, unicode(render.registrar(form)))

    def test_registrar_POST_redireccion(self):
        db = web.database(dbn='sqlite', db='myweb.db')
        cant_clientes = DataBase().longitud_cliente(db.select('cliente'))

        usuario = {'usuario': 'naranja'}
        data = urllib.urlencode(usuario)
        request = app.request('/registrar', method='POST', data=data)

        incremento_cliente = DataBase().longitud_cliente(db.select('cliente'))
        assert incremento_cliente > cant_clientes, 'Se esperaba que %d fuese mayor que %d' % (incremento_cliente, cant_clientes)

        db.delete('cliente', where='id=' + str(incremento_cliente))

        self.assert_es_status('303 See Other', request.status)

class TestUsuario(CasoTest):
    pass

class DataBase:

    def seleccionar_en_db(self):
        db = web.database(dbn='sqlite',db='myweb.db')

        cliente = db.select('cliente')
        nombre = 'horacio'
        assert cliente.__getitem__(0).get('nombre') == nombre, 'Se esperaba que %r fuese igual a %r' % (cliente, nombre)

    def insertar_en_db(self):
        db = web.database(dbn='sqlite', db='myweb.db')

        cliente = db.select('cliente')
        cant_clientes = self.longitud_cliente(cliente)
        cliente_insertar = db.insert('cliente', id=cant_clientes+1, nombre='cuasi')

        var = 'id=' + str(cant_clientes+1)
        cliente = db.select('cliente', where=var)
        nombre = 'cuasi'
        assert cliente.__getitem__(0).get('nombre') == nombre, 'Se esperaba que %r fuese igual a %r' % (cliente.__getitem__(0).get('nombre'), nombre)

        cliente = db.select('cliente')
        cliente = self.longitud_cliente(cliente)
        assert cant_clientes != cliente, 'Se esperaba %r y se obtuvo %r.' % (cant_clientes, cliente)

        self.borrar_entrada_en_db()

    '''###################################################################'''

    def entrada_en_db(self):
        db = web.database(dbn='sqlite', db='myweb.db')
        cliente = db.select('cliente')
        cant_clientes = self.longitud_cliente(cliente)

        var = 'id='+str(cant_clientes)
        cliente = db.delete('cliente', where=var)

        cliente = db.select('cliente')
        cliente = self.longitud_cliente(cliente)
        assert cant_clientes != cliente, 'Se esperaba %r y se obtuvo %r.' % (cant_clientes, cliente)

    def longitud_cliente(self,cliente):
        cant = 0
        for i in cliente:
            cant += 1
        return cant


if __name__ == '__main__':
    import web
    db = web.database(dbn='sqlite',db='myweb.db')
    cliente = db.select('cliente')

    # TestDataBase().borrar_entrada_en_db()
    # TestDataBase().borrar_entrada_en_db()
