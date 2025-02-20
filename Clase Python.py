path = "../home/Estudiante/"
f = open('datame.txt', 'rt')

nombre_archivo = '/home/Estudiante/Descargas/Archivos Clase 01-20250128/cronograma_sugerido.csv'
b = []
with open(nombre_archivo, 'rt') as file:
next(file)
for line in file:
datos_linea = line.split(',')
print(datos_linea[1])
b.append(datos_linea[1])
print(b)

def generala_tirar():
res = []
while(len(res) < 5):
res.append(random.randint(1, 6))
return res
print(generala_tirar())

import numpy as np
import pandas as pd

# def pisar_elemento(M,e):

fname = '/home/Estudiante/Descargas/Archivos Clase 01-20250128/cronograma_sugerido.csv'
df = pd.read_csv(fname)

df.iloc[2:6]

datos = '/home/Estudiante/Descargas/Clase 02 - archivos-20250128/Clase-02-Actividad-01-Datos.csv'
df = pd.read_csv(datos)

df.columns
df.iloc[1:8]

encuesta = '/home/Estudiante/Descargas/Clase-02-Actividad-02-EncuestaDeMovilidad (respuestas).xlsx'
df = pd.read_excel(encuesta)