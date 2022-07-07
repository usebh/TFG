#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:01:34 2022

@author: eusebiobermejohiguera
Programa en Python para analizar uso protocolos de comunicación 
de las capturas de los sistemas DCS de diferentes plantas industriales
"""
import pandas as pd
import csv
import sweetviz
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

from autoviz.AutoViz_Class import AutoViz_Class #Instantiate the AutoViz class
AV = AutoViz_Class()

def ejercicio1 (ruta):
    dataframe = pd.read_csv(ruta)
    return dataframe
    
ruta = "ADCSV.csv"   
dataframe = ejercicio1(ruta)    

"""
Crea otra función llamada ejercicio2. Esta función recibe un único argumento que es un dataframe.
En concreto debe recibir el dataframe que se ha obtenido de leer el dataset WSCSV.

"""


print (dataframe)

"""
Protocol = dataframe["Protocol"]
Length = dataframe["Length"]



plt.xlabel("Length" , fontsize=18)
plt.ylabel("Protocol" , fontsize=16)
plt.scatter(Protocol, Length)
plt.plot(Protocol, Length)
plt.show()
"""
dataframe.groupby('Protocol').count()["Info"].plot(kind='bar')
##dataframe.groupby('Source').count()["Info"].plot(kind='bar')
##dataframe.groupby('Destination').count()["Info"].plot(kind='bar')

df = AV.AutoViz('ADCSV.csv')
df = AV.AutoViz('ADCSV.csv', depVar='Protocol')
df = AV.AutoViz('ADCSV.csv', depVar='Destination')


dataframe.to_csv("ADCSV.csv", index=False)
    
filename = 'ADCSV.csv'

sep = ","
dft = AV.AutoViz(
    filename,
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=0,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,)

#dataframe  = AV.AutoViz('estaciones_madrid_202111.csv')
#my_report = sweetviz.analyze([dataframe,"ESTACION"], target_feat="O3")
