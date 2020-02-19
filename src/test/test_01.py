#! /usr/local/bin/python3

import unittest, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.helpers import Helpers
from src.page.home_page import HomePage


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.helpers = Helpers()
        cls.chrome_options = Options()
        cls.chrome_options.headless = False
        cls.driver = webdriver.Chrome(options=cls.chrome_options)

        cls.config = cls.helpers.read_json_file('./settings.json')

        cls.driver.get(cls.config['url'])
        cls.driver.maximize_window()

        cls.home_page = HomePage(cls.driver)

    def test_01(self):
        resultados = self.helpers.read_json_file('./resultados.json')

        fecha_inicio = self.config['fecha_inicio']
        fecha_fin = self.config['fecha_fin']

        while fecha_inicio != fecha_fin or fecha_fin == fecha_fin:
            self.driver.get(self.config['url_dated'].format(date=fecha_inicio))

            for loteria in self.config['loterias']:
                resultados.append(self.home_page.get_sorteo(loteria, fecha_inicio))

            fecha_inicio = datetime.strftime(datetime.strptime(fecha_inicio, '%d-%m-%Y') + timedelta(1), '%d-%m-%Y')

        self.helpers.export_json_file('./resultados.json', resultados)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()