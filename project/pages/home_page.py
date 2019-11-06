import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as EXEC

from project.locators.locators import Locators

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

        self.premio_span = Locators.premio_span
        self.loteria_fecha_span = Locators.loteria_premio_fecha_span

    def get_sorteo(self, loteria, fecha):
        """
        Retorna un diccionario del sorteo de una lotería.

        Argumentos
        ----------
        loteria : str
            Nombre de la lotería a buscar los premios.
        fecha : str
            Fecha del sorteo.
        """
        sorteo = {
            "loteria": loteria,
            "fecha": fecha,
            "primer_lugar": "",
            "segundo_lugar": "",
            "tercer_lugar": ""
        }

        for i in range(1, 4):
            try:
                premio = self.wait.until(EC.visibility_of_element_located((self.loteria_fecha_span[0],
                                                                           self.loteria_fecha_span[1].format(loteria=loteria,
                                                                                                             fecha=fecha,
                                                                                                             no_premio=str(i)))))
            except EXEC.TimeoutException:
                if i == 1:
                    sorteo['primer_lugar'] = 'N/A'
                elif i == 2:
                    sorteo['segundo_lugar'] = 'N/A'
                else:
                    sorteo['tercer_lugar'] = 'N/A'
            else:
                if i == 1:
                    sorteo['primer_lugar'] = premio.text
                elif i == 2:
                    sorteo['segundo_lugar'] = premio.text
                else:
                    sorteo['tercer_lugar'] = premio.text

        return(sorteo)