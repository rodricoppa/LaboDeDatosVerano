empleado_01 = [  
    [20222333, 45, 2, 20000], # Empleado 1
    [33456234, 40, 0, 25000], # Empleado 2
    [45432345, 41, 1, 10000] # Empleado 3
]

def superanSalarioActividad01(matriz, umbral):
    resultado = []
    for fila in matriz:
        if fila[3] > umbral:
            resultado.append(fila)
    return resultado

for fila in empleado_01:
    print(fila)

resultado = superanSalarioActividad01(empleado_01, 15000)
print("Empleados con salario mayor a 15000:")
for fila in resultado:
    print(fila)
   
# Implementar la funcion costo O(n) ya que es necesario recorrer toda la matriz, es decir las listas, de la lista empleados_01

# Ahora si tengo 5 filas. Si ahora tengo 5 filas tengo que recorrer las 5 filas de la matriz.

empleado_02 = [  
    [20222333, 45, 2, 20000], # Empleado 1
    [33456234, 40, 0, 25000], # Empleado 2
    [45432345, 41, 1, 10000], # Empleado 3
    [43967304, 37, 0, 12000], # Empleado 4
    [42236276, 36, 0, 18000] # Empleado 5
]

for fila in empleado_02:
    print(fila)
   
# Sigue funcionando la funcion    

resultado = superanSalarioActividad01(empleado_02, 15000)
print("Empleados con salario mayor a 15000:")
for fila in resultado:
    print(fila)
 
# Ahora invierto el orden de las columnas
   
empleado_03 = [  
    # DNI, Salario, Edad, Hijos
    [20222333, 20000, 45, 2], # Empleado 1
    [33456234, 25000, 40, 0], # Empleado 2
    [45432345, 10000, 41, 1], # Empleado 3
    [43967304, 12000, 37, 0], # Empleado 4
    [42236276, 18000, 36, 0] # Empleado 5
]

for fila in empleado_03:
    print(fila)

resultado = superanSalarioActividad01(empleado_03, 15000)
print("Empleados con salario mayor a 15000:")
for fila in resultado:
    print(fila)

# No funciona ya que ahora en la columna 4 (el indice 3) no esta el salario sino que esta la cantidad de hijos.

def superanSalarioActividad03(matriz, umbral):
    resultado3 = []
    for fila in matriz:
        if fila[1] > umbral:
            # Reconstruimos la fila con el orden original [DNI, Edad, Hijos, Salario]
           resultado3.append([fila[0], fila[2], fila[3], fila[1]])  # Orden original
    return resultado3


resultado3 = superanSalarioActividad03(empleado_03, 15000)
print("Empleados con salario mayor a 15000:")
for fila in resultado3:
    print(fila)
   
# Ahora la implemento como una lista de columnas (en vez de filas)

empleado_04 = [
    [20222333, 33456234, 45432345, 43967304, 42236276], # DNI
    [45, 40, 41, 37, 36], # Edad
    [2, 0, 1, 0, 0], # Hijos
    [20000, 25000, 10000, 12000, 18000] # Salario
]

for fila in empleado_04:
    print(fila)

resultado = superanSalarioActividad01(empleado_04, 15000)
print("Empleados con salario mayor a 15000:")
for fila in resultado:
    print(fila)
   
# En este caso me devuelve la primer fila ya que esta agarrando el tercer valor y como el DNI
# es mayor a 15000 devuelve toda esta fila.

resultado3 = superanSalarioActividad03(empleado_04, 15000)
print("Empleados con salario mayor a 15000:")
for fila in resultado3:
    print(fila)

# En este caso me esta devolviendo las dos filas en las que el valor supera a 15000 ( el del DNI y el primer valor de salario)
# Y me hace el reacomodamiento de los valores en cada fila. Pero no es lo que quiero

def superanSalarioActividad04(matriz, umbral):
    # Extraigo la columna de los salarios
    salarios = empleado_04[3]
   
    #Aca almaceno los empleados que cumplen la condicion
    resultado4 = []
   
    for i in range(len(salarios)):
        if salarios[i] > umbral:
            # Extraigo los datos respetando el orden original
            empleado = [
                empleado_04[0][i],
                empleado_04[1][i],
                empleado_04[2][i],
                empleado_04[3][i]
            ]
           
            resultado4.append(empleado)
   
    return resultado4

resultado4 = superanSalarioActividad04(empleado_04, 15000)
print("Empleados con salario mayor a 15000:")
for fila in resultado4:
    print(fila)

# Pregunta1
# En el prmer caso al agregar mas filas a la amtriz la funcion superanSalarioActividad01 siguió funcionando

# En el caso en el que se alteraron el orden de las columnas hubo que armar una nueva función ya que no accedia al indice
# de salarios sino al de los hijos. Y en esta nueva funcion cuando el valor del salario que ahora esta en el indice 1
# es mayor al umbral, armo la nueva matrriz con el orden original de las columnas

# Pregunta2
# Cuando se cambio la matriz de lista de filas a lista de columnas, tampoco funcionaron las funciones ya hechas, ya que para
# superanSalarioACtividad01 al acceder al indice 3, ahora accedo al DNi en la primer fila  me devuelve toda esa fila, cosa que
# no quiero, luego para la funcion superanSalarioACtividad03 al acceder al indice 1 de la amtriz me va a dar que ahora el DNI y
# el salario en ese indice superna al umbral pero me devulve toda esa fila (la primera con todos los DNIs y la segunda con todos
# los salarios). Por lo que en la funcion nueva debo sacar la fila de los salarios y ver si estos superan a cierto umbral,
# y en los que los supera armar la matriz nueva con DNI, edad, hijos y salario.

