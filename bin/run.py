import web
from web import form
from app.db import BaseDatos

urls = (
    '/', 'Index',
    '/form', 'Form',
    '/registrar', 'Registrar',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

registrar_form = form.Form(
    form.Textbox('usuario', description='usuario')
    )

class Index:

    def GET(self):
        todos = BaseDatos().todo_elemento_tabla('myweb.db', 'cliente')
        return render.index(todos)

class Form:

    def GET(self):
        return render.form()

    def POST(self):
        salida = web.input('dato')
        valor = salida.dato
        return valor

class Registrar:

    def GET(self):
        form = registrar_form()
        return render.registrar(form)

    def POST(self):
        salida = web.input('usuario')
        valor = salida.usuario

        db = web.database(dbn='sqlite', db='myweb.db')
        cliente = db.select('cliente')
        cant_clientes = BaseDatos().contar_cant_clientes(cliente)

        db.insert('cliente', id=cant_clientes+1, nombre=valor)

        raise web.seeother('/')

if __name__ == '__main__':
    app.run()
