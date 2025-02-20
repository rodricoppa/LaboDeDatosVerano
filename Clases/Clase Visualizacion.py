#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:01:54 2025

@author: Estudiante
"""
#%% Librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Datos de vinos
carpeta = "/home/Estudiante/Descargas/Clase 11-12 - Archivos-20250213/"

data_vinos = pd.read_csv(carpeta + "wine.csv", sep = ";")

print(data_vinos)

#%% grafico de dispersion/de puntos
plt.scatter(data = data_vinos, x = "fixed acidity", y ="citric acid")

fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"
ax.scatter(data = data_vinos,
            x = "fixed acidity",
            y = "citric acid",
plt.scatter(data = data_vinos, x = "pH", y ="chlorides")

fig, ax = plt.subplots()

tamanoBurbuja = 5
plt.rcParams["font.family"] = "sans-serif"
ax.scatter(data = data_vinos,
            x = "pH",
            y = "chlorides",
            s = data_vinos["chlorides"]*tamanoBurbuja)


ax.set_title("ph vs Acidez volatil")
ax.set_xlabel("pH (g/dm3)")
ax.set_ylabel("Contenido de acidez volatil (g/dm3)", fontsize = "medium")

            s = 8,
            color = "magenta")

ax.set_title("Acidez vs contenido de ácido cítrico")
ax.set_xlabel("Acidez (g/dm3)")
ax.set_ylabel("Contenido de ácido cítrico (g/dm3)", fontsize = "medium")

#%% Datos de arboles
carpeta_arboles = "/home/Estudiante/Descargas/"

data_arboles = pd.read_csv("arbolado-en-espacios-verdes.csv", sep = ",", index_col = 2)

print(data_arboles)

# 17 variables
# 51502 filas

plt.scatter(data = data_arboles, x = 'primer_atributo', y = 'segundo_atributo')
lista_de_especies = list(data_arboles['nombre_com'].value_counts().index)[0:30]
especies_mas_frecuentes = data_arboles[data_arboles['nombre_com'].isin(lista_de_especies)]

# %% grafico de altura vs diametro
fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"
ax.scatter(data = especies_mas_frecuentes,
            x = "altura_tot",
            y = "diametro",
            s = 8,
            color = "magenta")

ax.set_title("Altura vs Diametro")
ax.set_xlabel("Altura")
ax.set_ylabel("Diametro")

# %% grafico de long-lat

fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"
ax.scatter(data = especies_mas_frecuentes,
            x = "long",
            y = "lat",
            s = 8,
            color = "magenta")

ax.set_title("Longitud vs Latitud")
ax.set_xlabel("Longitud")
ax.set_ylabel("Latitud")

# %% Grafico de burbujas

fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"

tamanoBurbuja = 5
ax.scatter(data = data_vinos,
            x = "fixed acidity",
            y = "citric acid",
            s = data_vinos["residual sugar"]*tamanoBurbuja)

ax.set_title("Relación entre tres variables")
ax.set_xlabel("Acidez (g/dm3)", fontsize = "medium")
ax.set_ylabel("Contenido de ácido cítrico (g/dm3)", fontsize = "medium")

#%% grafico de torta

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'

plt.rcParams['font.size'] = 9.0

data_vinos['type'].value_counts().plot(kind = 'pie',
                   ax = ax,
                   autopct = '%1.1f%%',
                   colors = ['#66b3ff', '#ff9999'],
                   startangle = 90,
                   shadow = True,
                   explode = (0.1, 0),
                   legend = False
                   )
plt.scatter(data = data_vinos, x = "fixed acidity", y ="citric acid")

fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"
ax.scatter(data = data_vinos,
            x = "fixed acidity",
            y = "citric acid",
            s = 8,
            color = "magenta")

ax.set_title("Acidez vs contenido de ácido cítrico")
ax.set_xlabel("Acidez (g/dm3)")
ax.set_ylabel("Contenido de ácido cítrico (g/dm3)", fontsize = "medium")
ax.set_ylabel('')
ax.set_title('Distribución de tipos de vinos')

# %% Grafico entre pH y Acidez

fig, ax = plt.subplots()

tamanoBurbuja = 5
plt.rcParams["font.family"] = "sans-serif"
ax.scatter(data = data_vinos,
            x = "pH",
            y = "chlorides",
            s = data_vinos["chlorides"]*tamanoBurbuja)

ax.set_title("ph vs Cloruros")
ax.set_xlabel("pH (g/dm3)")
ax.set_ylabel("Contenido de Cloruro (g/dm3)", fontsize = "medium")

fig.savefig('')

#%% Grafico de barras

data_Cheetah = pd.read_csv(carpeta + "cheetahRegion.csv", sep = ",")

fig, ax = plt.subplots() 

plt.rcParams['font.family'] = "sans-serif"

ax.bar(data = data_Cheetah, x = 'Anio', height = 'Ventas')

ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize = 'medium')
ax.set_ylabel('Ventas (millones de $', fontsize = 'medium')
ax.set_xlim(0, 11)
ax.set_ylim(0, 250)

ax.set_xticks(range(1,11,1))
ax.set_yticks([])
ax.bar_label(ax.containers[0], fontsize = 8)

# %%Grafico de barras agrupadas

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'

data_Cheetah.plot(x = 'Anio',
                   y = ['regionEste', 'regionOeste'],
                   kind = 'bar',
                   label = ['Region Este', 'Region Oeste'],
                   ax = ax)

# %% Grafico de barras apiladas

fig, ax = plt.subplots()

ax.bar(data_Cheetah['Anio'], data_Cheetah['regionEste'],
       label = 'Region Este', color = "#4A4063")
ax.bar(data_Cheetah['Anio'], data_Cheetah['regionOeste'], 
       bottom = data_Cheetah['regionEste'], label = 'Region Oeste',
       color = 'skyblue')

# %% Grafico de líneas

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'

ax.plot('Anio', 'Ventas', data = data_Cheetah, marker = "o")

ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize = 'medium')
ax.set_ylabel('Ventas (millones de $)', fontsize = 'medium')
ax.set_xlim(0, 12)
ax.set_ylim(0, 250)

# %% Distribucion de Datos categóricos

fig, ax = plt.subplots()

gaseosas = pd.read_csv(carpeta + 'gaseosas.csv')
gaseosas['Compras_gaseosas'].value_counts(normalize = True).plot.bar(ax = ax)

ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_xlabel('Marcas de gaseosas')
ax.set_yticks([])
ax.bar_label(ax.containers[0], fontsize = 8)
ax.tick_params(axis = 'x', labelrotation = 0)

# %% Histogramas

import seaborn as sns

ageAtDeath = pd.read_csv(carpeta + 'ageAtDeath.csv')

fig, ax = plt.subplots()

sns.histplot(data = ageAtDeath['AgeAtDeath'], bins = 17)

# %% Histograma de propinas

import duckdb as dd

carpeta_tips = "/home/Estudiante/Descargas/"

tips = pd.read_csv("tips.csv")

propina_hombres = dd.sql("""
                    SELECT tip, day
                    FROM tips 
                    WHERE sex = 'Male'
                  """).df()
                  
propina_mujer = dd.sql("""
                       SELECT tip, day
                       FROM tips
                       WHERE sex = 'Female'
                """).df() 

fig, ax = plt.subplots()

sns.histplot(data = tips, x = 'tip', hue = 'sex')

# %% Boxplot

carpeta_venta_casas = "/home/Estudiante/Descargas/"

venta_casas = pd.read_csv("ventaCasas.csv")

fig, ax = plt.subplots()

ax.boxplot(venta_casas['PrecioDeVenta'], showmeans=True)

# Agrega título, etiquetas a los ejes
# y limita el rango de valores de los ejes
ax.set_title('Precio de venta de casas')
ax.set_xticks([])
ax.set_ylabel('Precio de venta ($)')
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("$ {x:,.2f}"))
ax.set_ylim(0, 500)

# %% Boxplot propinas
ax = sns.boxplot(x = 'day',
                 y = 'tip',
                 hue = 'sex',
                 data = tips,
                 order = ['Thur', 'Fri', 'Sat', 'Sun'],
                 palette = {"Female": "orange", "Male": "skyblue"})

ax.set_title("Propinas")
ax.set_xlabel('Día de la Semana')
ax.set_ylabel('Valor de propina ($)')
ax.set_ylim(0, 12)
ax.legend(title = 'Sexo')
ax.set_xticklabels(['Jueves', 'Viernes', 'Sábado', 'Domingo'])

# %% Violinplot

ax = sns.violinplot(x = "sex", y = "tip", data = tips,
                    palette = {"Female": "orange", "Male": "skyblue"})

ax.set_title('Propinas')
ax.set_xlabel('sexo')
ax.set_ylabel('Valor de propina ($)')
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.2f}"))
ax.set_ylim(0, 12)
ax.set_xticketlabels(['Femenino', 'Masculino'])
