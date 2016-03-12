import sqlite3

class BaseDatos:

    def __init__(self):
        pass

    def realizar_commit(self, nomb_DB):
        ''' Guarda todo los cambios realizados '''
        nomb_DB.commit()

    ''' ############################################################### '''

    def conectar_BD(self, nomb):
        nombre_DB = sqlite3.connect(nomb)
        return nombre_DB

    def cursor_BD(self, DB_nombre):
        consulta = DB_nombre.cursor()
        return consulta

    def todo_elemento_tabla(self, nomb_DB, nomb_TABLA):
        ''' Retorna todos los elementos de la tabla '''

        nombre_DB = self.conectar_BD(nomb_DB)
        consulta_DB = self.cursor_BD(nombre_DB)

        todos = consulta_DB.execute('SELECT * FROM %s' % (nomb_TABLA))
        return todos

    def contar_cant_clientes(self, clientes):
        num = 0
        for i in clientes:
            num += 1
        return num

        ''' ############################################################### '''

    def main(self):
        ''' Este es un metodo de ejemplo consulta '''

        nombre_DB = self.conectar_BD('myweb.db')
        consulta_DB = self.cursor_BD(nombre_DB)

        # self.agregarCliente('horacio')
        # nombre_Db.commit()

        todos = consulta_DB.execute('SELECT * FROM cliente')
        for i in todos: print i

class CrearTabla:

    def __init__(self):
        pass

    def crear_T(self, nomb_BD):
        nomb_BD = BaseDatos().conectar_BD(nomb_BD)
        crear = BaseDatos().cursor_BD(nomb_BD)
        crear.execute('''CREATE TABLE cliente (id INTEGER PRIMARY KEY, nombre TEXT)''')

    def agregar_C(self, num, nomb, nomb_BD):
        nomb_BD = BaseDatos().conectar_BD(nomb_BD)
        agregar = BaseDatos().cursor_BD(nomb_BD)
        agregar.execute("INSERT INTO cliente (id, nombre) VALUES (?,?)",(num, nomb))

    def crear_Tabla(self, nomb_BD, nombre_TABLA, *args):
        ''' Se necesita primero una base de datos para crear un tabla '''
        nombre_BD = BaseDatos().conectar_BD(nomb_BD)
        crear = BaseDatos().cursor_BD(nombre_BD)
        todos = ''
        for arg in args:
            for modelo in arg:
                todos += modelo
        # Creo la TABLA.
        i = 'CREATE TABLE '+ nombre_TABLA + ' ('+ todos +')'
        crear.execute(i)

    def insertar_Columna(self, nomb_BD, nomb_TABLA, *args):
        ''' Se necesita primero una tabla para crear un columna '''
        nombre_BD = BaseDatos().conectar_BD(nomb_BD)
        agregar = BaseDatos().cursor_BD(nombre_BD)

        todos,cont = ('','')
        for arg in args:
            for modelo in arg:
                # Obtengo el nombre de la variable de la BD.
                modelo = modelo.split(' ')
                todos += modelo[0] + ','
                cont += '?,'

        'OJO INGRASO VALORES ESTATICO!!'
        insertar = 'INSERT INTO '+ nomb_TABLA + ' (' + todos + ') VALUES ' + '(' + cont + ')', (0,'lucho','lucho')

class CrearModelo:

    def __init__(self):
        pass

    def columnas_Int(self, nombre, primary_key = False):
        if  not primary_key:
            respuesta = nombre + ' INT '
        else:
            respuesta = nombre + ' INT ' + ' PRIMARY KEY '
        return respuesta

    def columnas_Text(self, nombre, primary_key = False):
        if  not primary_key:
            respuesta = nombre + ' TEXT '
        else:
            respuesta = nombre + ' TEXT ' + ' PRIMARY KEY '
        return respuesta

    def columna_Real(self, nombre, primary_key = False):
        if  not primary_key:
            respuesta = nombre + ' REAL '
        else:
            respuesta = nombre + ' REAL ' + ' PRIMARY KEY '
        return respuesta

    def obtener_modelos(self, mod_creado):
        ''' Obtengo las variables que utilizare para crear la BD '''
        modelos = dir(mod_creado)
        objeto = dir(CrearModelo)
        diff = []
        for mod in modelos:
            for obj in objeto:
                esta = False
                if mod == obj:
                    esta = True
                    break;
            if not esta:
                diff.append(mod)
        return diff

    def es_una_subclase(self, nombre):
        ''' Determinar si es una subclase la app instalada '''
        return issubclass(nombre, CrearModelo)


if __name__ == '__main__':

    import inspect
    print inspect.isclass(Hola)
    print issubclass(Hola, CrearModelo)
    print CrearModelo().obtener_modelos(dir(Hola))
