import web

urls = (
    '/', 'Index',
    '/form', 'Form',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return "Hola Mundo!"

class Form:
    def GET(self):
        return render.form()

    def POST(self):
        salida = web.input('dato')
        valor = salida.dato
        return valor

if __name__ == '__main__':
    app.run()
