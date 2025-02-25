#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:11:13 2025

@author: Estudiante
"""
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import math
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import tree

ruta= "/home/Estudiante/Descargas/"

# %% Alturas - Graficos de Regresion
datos = pd.read_csv(ruta + "Resultados - Altura - 2025v - Alturas(1).csv", index_col = 0)

datos_varones = datos[datos["Sexo al nacer (M/F)"] == "M"]
X = datos_varones[["altura madre"]]

alturas = datos[["Altura (cm)"]]
Y = alturas[datos["Sexo al nacer (M/F)"] == "M"]

neigh = KNeighborsRegressor(n_neighbors = 5)
neigh.fit(X, Y)

datonuevo = pd.DataFrame([{"altura madre": 156}])
neigh.predict(datonuevo)
Y_pred = neigh.predict(X)
mean_squared_error(Y, Y_pred)

eje_x = []
errores = []
for i in range(1, 21):    
    neigh = KNeighborsRegressor(n_neighbors = i)
    neigh.fit(X, Y)
    datonuevo = pd.DataFrame([{"altura madre": 156}])
    neigh.predict(datonuevo)
    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    errores.append(math.floor(error))
    eje_x.append(i)
    
print(errores)

plt.plot(eje_x, errores)
plt.scatter(eje_x, errores)
plt.grid()
plt.xlabel("K_Neighbors")
plt.ylabel("Errores")
plt.show()

# %%===========================================================================
# mpg
# =============================================================================

mpg = pd.read_csv("Clase 16 - RLS - Archivos clase-20250225/auto-mpg.xls")

X = mpg[["acceleration", "weight"]]

Y = mpg[["mpg"]]


def graficarErrores(X, title):
    eje_x = []
    errores = []
    for i in range(1, 21):    
        neigh = KNeighborsRegressor(n_neighbors = i)
        neigh.fit(X, Y)
        Y_pred = neigh.predict(X)
        error = mean_squared_error(Y, Y_pred)
        errores.append(math.floor(error))
        eje_x.append(i)
    
   
    print(errores)

    plt.plot(eje_x, errores)
    plt.scatter(eje_x, errores)
    plt.grid()
    plt.xlabel("K_Neighbors")
    plt.ylabel("Errores")
    plt.show()

# %%

sns.pairplot(mpg[["horsepower", "model year", "acceleration"]])

# %%
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2) 


errores_train = []
errores_test = []
for k in range(1, 21):
    modelo = KNeighborsRegressor(n_neighbors = k)
    modelo.fit(X_train, Y_train)
    Y_pred_train = modelo.predict(X_train)
    Y_pred_test = modelo.predict(X_test)   
    error_train = mean_squared_error(Y_train, Y_pred_train)
    error_test = mean_squared_error(Y_test, Y_pred_test)
    errores_train.append(error_train)
    errores_test.append(error_test)
    
plt.figure(figsize = (10, 6))
plt.plot(list(range(1, 21)),
         errores_train, label = "train")
plt.plot(list(range(1, 21)),
         errores_test, label = "test")
plt.legend()
plt.xticks(list(range(1, 21)))

plt.xlabel("Cantidad de vecinos")
plt.ylabel("MSE")
plt.title("MSE segun cantidad de vecinos")
plt.grid()

#%%

X = mpg[["acceleration"]]
y = mpg[["mpg"]]
#%% separamos entre dev y eval
X_dev, X_eval, y_dev, y_eval = train_test_split(X,y,test_size=0.1, random_state = 20)

#%% experimento

alturas = [1,2,3,5,10]
nsplits = 5
kf = KFold(n_splits=nsplits)

resultados = np.zeros((nsplits, len(alturas)))
# una fila por cada fold, una columna por cada modelo

eje_x = []
errores = []
for i, (train_index, test_index) in enumerate(kf.split(X_dev)):

    kf_X_train, kf_X_test = X_dev.iloc[train_index], X_dev.iloc[test_index]
    kf_y_train, kf_y_test = y_dev.iloc[train_index], y_dev.iloc[test_index]
    
    for j, hmax in enumerate(alturas):
        neigh = KNeighborsRegressor(n_neighbors = i)
        neigh.fit(X, y)
        Y_pred = neigh.predict(X)
        error = mean_squared_error(Y, Y_pred)
        errores.append(math.floor(error))
        eje_x.append(i)
        
        score = accuracy_score(kf_y_test,pred)   
        resultados[i, j] = score
#%% promedio scores sobre los folds
scores_promedio = resultados.mean(axis = 0)


#%% 
for i,e in enumerate(alturas):
    print(f'Score promedio del modelo con hmax = {e}: {scores_promedio[i]:.4f}')

#%% entreno el modelo elegido en el conjunto dev entero
arbol_elegido = tree.DecisionTreeClassifier(max_depth = 1)
arbol_elegido.fit(X_dev, y_dev)
y_pred = arbol_elegido.predict(X_dev)

score_arbol_elegido_dev = accuracy_score(y_dev, y_pred)
print(score_arbol_elegido_dev)

#%% pruebo el modelo elegid y entrenado en el conjunto eval
y_pred_eval = arbol_elegido.predict(X_eval)       
score_arbol_elegido_eval = accuracy_score(y_eval, y_pred_eval)
print(score_arbol_elegido_eval)

