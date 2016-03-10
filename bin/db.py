import sqlite3

crearDb = sqlite3.connect('myweb.db')
query = crearDb.cursor()

def crearTable():
    query.execute('''CREATE TABLE cliente (id INTEGER PRIMARY KEY, nombre TEXT)''')

def agregarCliente(nomb):
    query.execute("INSERT INTO cliente (id, nombre) VALUES (?,?)",(1,nomb))

def main():
    # crearTable()
    agregarCliente('horacio')
    crearDb.commit()

    query.execute('SELECT * FROM cliente')

if __name__ == '__main__':
    main()
    # agregarCliente('horacio')
    # query.execute('SELECT * FROM cliente')
    for i in query:
        print i