import sqlite3

class BaseDatos:

    def crearTable(self, nomb_BD):
        nomb_BD = self.conectar_BD(nomb_BD)
        crear = self.cursor_BD(nomb_BD)
        crear.execute('''CREATE TABLE cliente (id INTEGER PRIMARY KEY,
                                                nombre TEXT)''')

    def agregarCliente(self, num, nomb):
        nomb_BD = self.conectar_BD(nomb_BD)
        agregar = self.cursor_BD(nomb_BD)
        agregar.execute("INSERT INTO cliente (id, nombre) VALUES (?,?)",(num, nomb))

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

if __name__ == '__main__':
    BaseDatos().main()
