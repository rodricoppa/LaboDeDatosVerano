import csv

nombre_archivo = 'arbolado-en-espacios-verdes.csv'

def leer_parque(nombre_archivo, parque):
    lista_arboles = []
    
    with open(nombre_archivo, 'rt') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            if fila["espacio_ve"] == parque:  # Se asume que la columna del parque se llama "espacio_ve"
                lista_arboles.append(fila)
    
    return lista_arboles

# Prueba con el parque 'GENERAL PAZ'
parque = "GENERAL PAZ"
arboles_general_paz = leer_parque(nombre_archivo, parque)

# Mostrar cantidad de árboles encontrados
print(f"Cantidad de árboles en {parque}: {len(arboles_general_paz)}")

def especies(lista_arboles):
    """Devuelve el conjunto de especies presentes en la lista de árboles."""
    return {arbol["nombre_com"] for arbol in lista_arboles}

# Obtener las especies del parque 'GENERAL PAZ'
especies_general_paz = especies(arboles_general_paz)

# Mostrar el conjunto de especies encontradas
print(f"Especies encontradas en GENERAL PAZ ({len(especies_general_paz)} especies):")
print(especies_general_paz)
