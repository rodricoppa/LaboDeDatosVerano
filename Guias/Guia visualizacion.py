## Guia visualizacion de datos

import seaborn as sns
import matplotlib.pyplot as plt

data_ping = sns.load_dataset('penguins')

# a_ ¿Qué representa cada línea del dataframe?
# cada linea del dataframe representa un pinguino 

# b_ ¿Cuántas muestras hay en total?
# 344

# c_ ¿Cuáles son las especies de pingüinos consideradas?
# Adele, Chinstrap y Gentoo

# d_ ¿Cuáles son las islas estudiadas?
# Torgersen, Biscoe y Dream

# Para cada pingüino, ¿con qué datos contamos?
# species(especie), island(isla), bill_length_mm(longitud del pico), 
# bill_depth_mm(profundidad del pico), flipper_lenght_mm (longitud de la aleta),
# body_mass_g(masa corporal), sex (sexo)

# %% # Contar el número de pingüinos de cada especie por isla
distribucion_especies_isla = data_ping.groupby(['island', 'species']).size().unstack()

# Mostrar la distribución
print(distribucion_especies_isla)

# %% Gráfico de barras
distribucion_especies_isla.plot(kind='bar', stacked=True)
plt.title('Distribución de especies por isla')
plt.xlabel('Isla')
plt.ylabel('Número de pingüinos')
plt.show()

#%% Gráfico de torta para cada isla

islas = data_ping['island'].unique()
print(f"Islas estudiadas: {islas}")

for isla in islas:
    datos_isla = data_ping[data_ping['island'] == isla]
    especies_isla = datos_isla['species'].value_counts()
    especies_isla.plot(kind='pie', autopct='%1.1f%%', title=f'Distribución de especies en {isla}')
    plt.ylabel('')
    plt.show() 
