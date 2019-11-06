#! /usr/local/bin/python3
import json
from datetime import datetime, timedelta

class Helpers:
    """
    Clase con métodos de soporte para el proyecto.
    """

    def read_json_file(self, path):
        """
        Método utilizado para leer un archivo extensión JSON.

        Argumentos
        -----------
        path : str
            Ruta donde se encuentra el archivo.

        Retorna
        -------
        jsonfile
            Archivo extensión JSON.
        """

        with open(path, encoding='utf-8') as f:
            return json.load(f)

    def export_json_file(self, path, diccionario):
        """
        Método utilizado para exportar un diccionario a un archivo extensión JSON.

        Argumentos
        ----------
        path : str
            Ruta donde se desea exportar el archivo.
        diccionario : dict
            Diccionario contener de la data a exportar.
        """

        with open('./resultados.json', 'w') as fp:
            json.dump(diccionario, fp)

    def get_yesterday_date(self):
        """Retorna la fecha del día anterior."""
        return(datetime.strftime(datetime.now() - timedelta(1), '%d-%m-%Y'))