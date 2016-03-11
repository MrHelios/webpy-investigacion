import web
from os.path import isfile
from db import CrearTabla, BaseDatos, CrearModelo

class TestDataBase:

    def __init__(self):
        self.nombre_bd = 'prueba'
        self.direccion_bd = '/home/lucho/workspace/webpy/' + self.nombre_bd

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

    ''' ############################################################### '''

    def test_crear_bd(self):
        BaseDatos().conectar_BD(self.nombre_bd)
        assert isfile(self.direccion_bd) == True, 'El archivo no existe en la direccion indicada %s' % self.direccion_bd

    def test_crear_tabla(self):
        bd_test = BaseDatos().conectar_BD(self.nombre_bd)
        bd_consulta_test = BaseDatos().cursor_BD(bd_test)

        assert CrearModelo().es_una_subclase(UsuarioTest), 'No es una subclase.'
        modelos = CrearModelo().obtener_modelos(UsuarioTest)
        assert len(modelos) == 3 ,' Se esperaba que '+ len(modelos) +' fuese 3.'

        CrearTabla().crear_Tabla(self.nombre_bd, 'usuario', modelos)

    def test_limpieza(self):
        from os import remove
        remove(self.direccion_bd)
        assert isfile(self.direccion_bd) == False, 'El archivo no fue borrado.'


class UsuarioTest(CrearModelo):
    num = CrearModelo().columnas_Int('id', primary_key= True)
    nombre = CrearModelo().columnas_Text('nombre')
    clave = CrearModelo().columnas_Text('clave')