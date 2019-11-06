#! /usr/local/bin/python3
import sys, os, json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from datetime import datetime, timedelta

from project.helpers import Helpers

helpers = Helpers()

fecha_inicio = '05-11-2019'
fecha_fin = '06-11-2019'

fecha_inicio_dt = datetime.strftime(datetime.strptime(fecha_inicio, '%d-%m-%Y'), '%d-%m-%Y')
fecha_fin_dt = datetime.strftime(datetime.strptime(fecha_fin, '%d-%m-%Y'), '%d-%m-%Y')

while fecha_inicio != fecha_fin:
    print(fecha_inicio)

    fecha_inicio = datetime.strftime(datetime.strptime(fecha_inicio, '%d-%m-%Y') + timedelta(1), '%d-%m-%Y')