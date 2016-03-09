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
        time.sleep(1)
        self.tearDown()

        # Revision Pagina Form
        self.setUp()
        self.navegador.get('http://localhost:8080/form')
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
