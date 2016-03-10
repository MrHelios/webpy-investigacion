from selenium import webdriver
import unittest

import time

class NuevoVisitorTest(unittest.TestCase):

    def setUp(self):
        self.navegador = webdriver.Firefox()

    def tearDown(self):
        self.navegador.quit()

    def test_start(self):
        # Revision Pagina Index
        self.navegador.get('http://localhost:8080')
        url_inicial = self.navegador.current_url

        redireccion = self.navegador.find_element_by_id('form')
        redireccion.send_keys('\n')

        url_final = self.navegador.current_url
        assert url_inicial != url_final, 'Se esperaban que las urls %s y %s fueran distintas' % (url_inicial, url_final)

        agregar = self.navegador.find_element_by_id('agregar_item')
        texto = 'Aca no pasa nada.'
        agregar.send_keys(texto)
        agregar.send_keys('\n')
        resultado = self.navegador.page_source
        assert texto == resultado, 'Se esperaba que %r fuese %r' % (texto, resultado)

    def test_registrar(self):
        self.navegador.get('http://localhost:8080')
        url_inicial = self.navegador.current_url

        redireccion = self.navegador.find_element_by_id('registrar')
        redireccion.send_keys('\n')

        url_final = self.navegador.current_url
        assert url_inicial != url_final, 'Se esperaban que las urls %s y %s fueran distintas' % (url_inicial, url_final)

        url_inicial = url_final

        agregar = self.navegador.find_element_by_tag_name('label')
        agregar.send_keys('cana fria')
        agregar.send_keys('\n')

        url_final = self.navegador.current_url
        assert url_inicial != url_final, 'Se esperaban que las urls %s y %s fueran distintas' % (url_inicial, url_final)

if __name__ == '__main__':
    unittest.main()
