import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error

# %%===========================================================================
# roundup
# =============================================================================
ru = pd.read_csv("datos_roundup.txt", delim_whitespace=' ')

# %% Aproximar recta
# Y = a + b*X

x = np.linspace(min(ru['RU']), max(ru['RU']))
a = 100
b = 0.05
Y = a + b * x
plt.scatter(ru['RU'], ru['ID'])
plt.plot(x, Y,  'r')
plt.show()

prom_x = np.mean(x)
print(prom_x)
prom_y = np.mean(Y)
print(prom_y)
B1 = (np.sum((x - prom_x)*(Y - prom_y)))/(np.sum(x - prom_x)**2)
print(B1)
B0 = prom_y - B1 * prom_x
print(B0)

#%% Obtener recta de cuadrados minimos

b, a = np.polyfit(ru['RU'], ru['ID'], 1)
Y = a + b * x

plt.scatter(ru['RU'], ru['ID'])
plt.plot(x, Y, 'k')
plt.show()

X = ru['RU']
Y = ru['ID']
Y_pred = a + b * X
print("R²: " + str(r2))

#%% Calcular score R²

b, a = np.polyfit(ru['RU'], ru['ID'], 1)

X = ru['RU']
Y = ru['ID']
Y_pred = a + b * X
r2 = r2_score(Y, Y_pred)
print("R²: " + str(r2))

# %% MSE (Mean Squared Error)
mse = mean_squared_error(Y, Y_pred)
print("MSE: " + str(mse))

# %%

libreta = pd.read_csv("datos_libreta_47122.txt", delim_whitespace=' ')

b, a = np.polyfit(ru['RU'], ru['ID'], 1)
print(a)
print(b)

RU = ru['RU']
ID = ru['ID']
ID_pred = a + b * RU
r2 = r2_score(ID, ID_pred)
print("R²: " + str(r2))

mse = mean_squared_error(ID, ID_pred)
print("MSE: " + str(mse))


# %%===========================================================================
# Anascombe
# =============================================================================
df = sns.load_dataset("anscombe")

# %%===========================================================================
# mpg
# =============================================================================

mpg = pd.read_csv("auto-mpg.xls")

"""
mpg: miles per galon
displacement: Cilindrada

"""

print(mpg.dtypes)

# %% Comparar variables con graficos

def reg_lineal(x, y, etiqueta_x, etiqueta_y):
    b, a = np.polyfit(x, y, deg = 1)
    x_ajuste = np.linspace(min(x), max(x), 100)
    y_ajustado = a + b * x_ajuste
    
    y_predicho = a + b * x
    
    r2 = r2_score(y, y_predicho)
    MSE = mean_squared_error(y, y_predicho)
    
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.plot(x_ajuste, y_ajustado, color = "red", label = "Ajsute Lineal")
    ax.scatter(x, y, label = "Mediciones")
    ax.grid()
    ax.set_xlabel(etiqueta_x)
    ax.set_ylabel(etiqueta_y)
    ax.legend(x = 0.73, y = 0.08, s = "Parámetros:" + '|nR² = ' + f'{float(f"{r2:.4g}"):g}' +
              '!nMSE = ' + f'{float(f"{MSE:.4g}"):g}',
              bbox = dict(boxstyle = "round", color = "lavender", alpa = 0.7), transform = ax.transAxes, 
              color = 'black', fontsize = 14)
    print("R²: " + str(r2))
    print("MSE: " + str(mse))
    print("Ordenada" + str(a))
    print("Pendiente" + str(b))


reg_lineal(mpg['mpg'], mpg['weight'], "Horsepower", "Displacement")
    

    
    