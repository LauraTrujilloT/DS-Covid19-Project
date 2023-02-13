import pandas as pd
import numpy as np
import datetime
from datetime import timedelta

"""Importing csv file"""

dfCasos1 = df = pd.read_csv('Casos1.csv')


column_names = list(dfCasos1.columns.values)
print(column_names)

"""Change names of headers"""

dfCasos1.rename(columns={'ID de caso':'id',
                        'Fecha de diagnóstico':'fecha',
                         'Ciudad de ubicación':'ciudad',
                         'Departamento o Distrito':'departamento',
                         'Atención**':'atencion',
                         'Edad':'edad', 'Sexo':'sexo', 'Tipo*':'tipo',
                         'País de procedencia':'pais_procedencia'},
               inplace=True)

"""Counting empty or nan values"""
print(dfCasos1.isnull().sum()) #non null values

"""change datatime values"""

dfCasos1['fecha'] = pd.to_datetime(dfCasos1.fecha, errors='ignore')

""" Replace values all lower letter on all columns"""

lowrnames_city = []


for i in dfCasos1['ciudad']:
    a = i.lower()
    lowrnames_city.append(a)

dfCasos1['ciudad'] = lowrnames_city

lower_tipo = []

for i in dfCasos1['tipo']:
    a = i.lower()
    lower_tipo.append(a)

dfCasos1['tipo'] = lower_tipo

lower_pais_procediencia = []

for i in dfCasos1['pais_procedencia']:
    a = i.lower()
    lower_pais_procediencia.append(a)

dfCasos1['pais_procedencia'] = lower_pais_procediencia

dfCasos1['sexo'] = dfCasos1['sexo'].replace({'F':'f', 'M':'m'})
dfCasos1['tipo'] = dfCasos1['tipo'].replace({'en estudio':'en_estudio'})
dfCasos1['pais_procedencia'] = dfCasos1['pais_procedencia'].replace({'estados unidos':'estados_unidos',
                                                                     'méxico':'mexico'})
print(dfCasos1)


