# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:26:03 2025

Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Ejercicios SQL
Autor  : Rodrigo Gustavo Coppa
Fecha  : 2025-02-05
"""

# Importamos bibliotecas
import pandas as pd
import duckdb as dd

# Leo el archivo
leerArchivos = r"C:\Users\Usuario\Downloads\Guía Práctica - SQL - Archivos adjuntos-20250205\\"

# Abro losdataFrames
casos           = pd.read_csv(leerArchivos + "casos.csv") 

departamento    = pd.read_csv(leerArchivos + "departamento.csv")

grupoEtario     = pd.read_csv(leerArchivos + "grupoetario.csv")

provincia       = pd.read_csv(leerArchivos + "provincia.csv")

tipoEvento      = pd.read_csv(leerArchivos + "tipoevento.csv")

#Ejericios

# A. Consultas sobre una tabla 

# a. Listar sólo los nombres de todos los departamentos que hay en la tabla 
#   departamento (dejando los registros repetidos). 

print(departamento)

consultaSQL = """
                SELECT descripcion
                FROM departamento
              """
             
dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

# b. Listar sólo los nombres de todos los departamentos que hay en la tabla 
# departamento (eliminando los registros repetidos). 

consultaSQL = """
                SELECT DISTINCT descripcion
                FROM departamento
              """
             
dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

# c. Listar sólo los códigos de departamento y sus nombres, de todos los 
# departamentos que hay en la tabla departamento. 

consultaSQL = """
                SELECT DISTINCT id, descripcion
                FROM departamento
              """
             
dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

# d. Listar todas las columnas de la tabla departamento. 

consultaSQL = """
                SELECT DISTINCT id, descripcion, id_provincia
                FROM departamento
              """
             
dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

# e. Listar los códigos de departamento y nombres de todos los departamentos
# que hay en la tabla departamento. Utilizar los siguientes alias para las 
# columnas: codigo_depto y nombre_depto, respectivamente. 

consultaSQL = """
                SELECT DISTINCT id AS codigo_depto, descripcion AS nombre_depto
                FROM departamento
              """
              
dataframeResultado = dd.sql(consultaSQL).df()

# f. Listar los registros de la tabla departamento cuyo código de provincia
# es igual a 54 
             
consultaSQL = """
                SELECT *
                FROM departamento
                WHERE id_provincia = 54
              """

dataframeResultado = dd.sql(consultaSQL).df()

# g. Listar los registros de la tabla departamento cuyo código de provincia 
# es igual a 22, 78 u 86. 

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE id_provincia = 22 OR id_provincia = 78 OR 
                id_provincia = 86
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#h. Listar los registros de la tabla departamento cuyos códigos de provincia
# se encuentren entre el 50 y el 59 (ambos valores inclusive).

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE id_provincia BETWEEN 50 AND 59
              """
              
dataframeResultado = dd.sql(consultaSQL).df()

#B. Consultas multitabla (INNER JOIN) 

#a. Devolver una lista con los código y nombres de departamentos, asociados
# al nombre de la provincia al que pertenecen. 

consultaSQL = """
                SELECT DISTINCT d.id, d.descripcion, p.descripcion AS provincia
                FROM departamento AS d
                INNER JOIN provincia AS p
                ON d.id_provincia = p.id
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# b. Devolver una lista con los código y nombres de departamentos, asociados
# al nombre de la provincia al que pertenecen. 

consultaSQL = """
                SELECT DISTINCT d.id, d.descripcion, p.descripcion AS provincia
                FROM departamento AS d
                INNER JOIN provincia AS p
                ON d.id_provincia = p.id
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# c. Devolver los casos registrados en la provincia de “Chaco”.

consultaSQL = """
                SELECT DISTINCT d.id, d.descripcion
                FROM departamento AS d
                INNER JOIN provincia AS p
                ON d.id_provincia = p.id
                WHERE p.descripcion = 'Chaco'
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# d. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo 
# cantidad supere los 10 casos.

consultaSQL = """
                SELECT DISTINCT d.id, d.descripcion, c.cantidad
                FROM departamento AS d
                INNER JOIN casos AS c ON c.id_depto = d.id
                INNER JOIN provincia as p ON p.id = d.id_provincia
                WHERE p.descripcion = 'Buenos Aires' AND c.cantidad > 10
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# C. Consultas multitabla (OUTER JOIN) 

#a. Devolver un listado con los nombres de los departamentos que no tienen
# ningún caso asociado. 

consultaSQL = """
                SELECT DISTINCT d.id, d.descripcion
                FROM departamento AS d
                LEFT OUTER JOIN casos AS c ON d.id = c.id_depto
                WHERE c.id_depto IS NULL OR c.id_depto = '';
              """              
# no me toma ni null ni las comillas. Puede que no haya ninguno

dataframeResultado = dd.sql(consultaSQL).df()

#b. Devolver un listado con los tipos de evento que no tienen ningún caso 
# asociado. 

consultaSQL = """
                SELECT DISTINCT e.id, e.descripcion
                FROM tipoEvento AS e
                LEFT OUTER JOIN casos AS c ON c.id_tipoevento = e.id
                WHERE c.id_tipoevento IS NULL
              """              

dataframeResultado = dd.sql(consultaSQL).df()

#D. Consultas resumen 

#a. Calcular la cantidad total de casos que hay en la tabla casos. 

consultaSQL = """
                SELECT COUNT(*) AS CantidadCasos
                FROM casos
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# b. Calcular la cantidad total de casos que hay en la tabla casos para cada 
# año y cada tipo de caso. Presentar la información de la siguiente manera: 
# descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso 
# (ascendente) y  año (ascendente).

consultaSQL = """
                SELECT e.descripcion AS tipo_de_caso, c.anio, 
                COUNT(*) AS cantidad_casos
                FROM casos AS c
                INNER JOIN tipoEvento AS e ON e.id = c.id_tipoevento
                GROUP BY e.descripcion, c.anio
                ORDER BY e.descripcion ASC, c.anio ASC
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# c. Misma consulta que el ítem anterior, pero sólo para el año 2019. 

consultaSQL = """
                SELECT e.descripcion AS tipo_de_caso, c.anio, 
                    COUNT(*) AS cantidad_casos
                FROM casos AS c
                INNER JOIN tipoEvento AS e ON e.id = c.id_tipoevento
                WHERE c.anio = 2019
                GROUP BY e.descripcion, c.anio
                ORDER BY e.descripcion ASC, c.anio ASC
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# d. Calcular la cantidad total de departamentos que hay por provincia. 
# Presentar la información ordenada por código de provincia. 

consultaSQL = """
                SELECT d.id_provincia, p.descripcion, 
                    COUNT(*) AS total_departamentos
                FROM departamento as d
                INNER JOIN provincia AS p ON d.id_provincia = p.id
                GROUP BY d.id_provincia, p.descripcion
                ORDER BY d.id_provincia 
              """              

dataframeResultado = dd.sql(consultaSQL).df()

#e. Listar los departamentos con menos cantidad de casos en el año 2019. 

consultaSQL = """
                SELECT d.id, d.descripcion AS departamentos, 
                    COUNT(*) AS total_casos
                FROM departamento as d
                INNER JOIN casos AS c ON c.id_depto = d.id
                WHERE c.anio = 2019 
                GROUP BY d.id, d.descripcion
                HAVING total_casos < 5
                ORDER BY total_casos
              """              

dataframeResultado = dd.sql(consultaSQL).df()

#f. Listar los departamentos con más cantidad de casos en el año 2020.

consultaSQL = """
                SELECT d.id, d.descripcion AS departamentos, 
                    COUNT(*) AS total_casos
                FROM departamento as d
                INNER JOIN casos AS c ON c.id_depto = d.id
                WHERE c.anio = 2020 
                GROUP BY d.id, d.descripcion
                HAVING total_casos > 100
                ORDER BY total_casos DESC
              """              

dataframeResultado = dd.sql(consultaSQL).df()

#g. Listar el promedio de cantidad de casos por provincia y año. 

consultaSQL = """
                SELECT p.id AS id_provincia, p.descripcion AS provincia, 
                    c.anio, AVG(c.cantidad) AS promedio_casos
                FROM provincia AS p
                INNER JOIN departamento AS d ON d.id_provincia = p.id
                INNER JOIN casos AS c ON c.id_depto = d.id
                GROUP BY p.id, p.descripcion, c.anio
                ORDER BY p.id ASC, c.anio ASC
              """              

dataframeResultado = dd.sql(consultaSQL).df()

# h. Listar, para cada provincia y año, cuáles fueron los departamentos que 
# más cantidad de casos tuvieron. 



#i. Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo
# la provincia de Buenos Aires en el año 2019. 

consultaSQL = """
                SELECT 
                    SUM(c.cantidad) AS total_casos,
                    MAX(c.cantidad) AS max_casos,
                    MIN(c.cantidad) AS min_casos,
                    AVG(c.cantidad) AS promedio_casos
                FROM provincia AS p
                INNER JOIN departamento AS d ON p.id = d.id_provincia
                INNER JOIN casos AS c ON d.id = c.id_depto
                WHERE p.descripcion = 'Buenos Aires' AND c.anio = 2019
              """

dataframeResultado = dd.sql(consultaSQL).df()

# j. Misma consulta que el ítem anterior, pero sólo para aquellos casos en 
# que la cantidad total es mayor a 1000 casos. 

consultaSQL = """
                SELECT 
                    SUM(c.cantidad) AS total_casos,
                    MAX(c.cantidad) AS max_casos,
                    MIN(c.cantidad) AS min_casos,
                    AVG(c.cantidad) AS promedio_casos
                FROM provincia AS p
                INNER JOIN departamento AS d ON p.id = d.id_provincia
                INNER JOIN casos AS c ON d.id = c.id_depto
                WHERE p.descripcion = 'Buenos Aires' AND c.anio = 2019
                GROUP BY p.id
                HAVING sum(c.cantidad) > 1000
              """

dataframeResultado = dd.sql(consultaSQL).df()

# E. Subconsultas (ALL, ANY) 

# a. Devolver el departamento que tuvo la mayor cantidad de casos sin hacer 
# uso de MAX, ORDER BY ni LIMIT. 

consultaSQL = """
                SELECT d.id, d.descripcion, c.cantidad
                FROM departamento AS d 
                INNER JOIN casos AS c ON d.id = c.id_depto
                WHERE c.cantidad >= ALL (
                    SELECT cantidad 
                    FROM casos
                )
              """

dataframeResultado = dd.sql(consultaSQL).df()

# b. Devolver los tipo de evento que tienen casos asociados. 
# (Utilizando ALL o ANY). 

consultaSQL = """
                SELECT te.id, te.descripcion
                FROM tipoEvento AS te
                WHERE te.id = ANY (
                    SELECT DISTINCT c.id_tipoevento 
                    FROM casos AS c
                )
              """

dataframeResultado = dd.sql(consultaSQL).df()

# F. Subconsultas (IN, NOT IN) 

# a. Devolver los tipo de evento que tienen casos asociados 
# (Utilizando IN, NOT IN). 

consultaSQL = """
                SELECT te.id, te.descripcion
                FROM tipoEvento AS te
                WHERE te.id IN (
                    SELECT DISTINCT c.id_tipoevento 
                    FROM casos AS c
                )
              """

dataframeResultado = dd.sql(consultaSQL).df()

# b. Devolver los tipo de evento que NO tienen casos asociados 
# (Utilizando IN, NOT IN). 

consultaSQL = """
                SELECT te.id, te.descripcion
                FROM tipoEvento AS te
                WHERE te.id NOT IN (
                    SELECT DISTINCT c.id_tipoevento 
                    FROM casos AS c
                )
              """

dataframeResultado = dd.sql(consultaSQL).df()

# G. Subconsultas (EXISTS, NOT EXISTS) 

# a. Devolver los tipo de evento que tienen casos asociados 
# (Utilizando EXISTS, NOT EXISTS). 

consultaSQL = """
                SELECT te.id, te.descripcion
                FROM tipoEvento AS te
                WHERE EXISTS (
                    SELECT 1 
                    FROM casos AS c
                    WHERE c.id_tipoevento = te.id
                )
              """

dataframeResultado = dd.sql(consultaSQL).df()

# b. Devolver los tipo de evento que NO tienen casos asociados 
# (Utilizando EXISTS, NOT EXISTS).

consultaSQL = """
                SELECT te.id, te.descripcion
                FROM tipoEvento AS te
                WHERE NOT EXISTS (
                    SELECT 1 
                    FROM casos AS c
                    WHERE c.id_tipoevento = te.id
                )
              """

dataframeResultado = dd.sql(consultaSQL).df()

# H. Subconsultas correlacionadas 

#a. Listar las provincias que tienen una cantidad total de casos mayor 
# al promedio de casos del país. Hacer el listado agrupado por año.

consultaSQL = """
                SELECT p.id, p.descripcion, c.anio, SUM(c.cantidad) AS total_casos
                FROM provincia AS p
                INNER JOIN departamento AS d ON p.id = d.id_provincia
                INNER JOIN casos AS c ON d.id = c.id_depto
                GROUP BY p.id, p.descripcion, c.anio
                HAVING SUM(c.cantidad) > (
                    SELECT AVG(total_casos_por_año)
                    FROM (
                        SELECT c.anio, SUM(c.cantidad) AS total_casos_por_año
                        FROM casos AS c
                        INNER JOIN departamento AS d ON c.id_depto = d.id
                        INNER JOIN provincia AS p ON d.id_provincia = p.id
                        GROUP BY c.anio
                    ) AS subquery
                    WHERE subquery.anio = c.anio
                )
                ORDER BY c.anio, total_casos DESC
              """

dataframeResultado = dd.sql(consultaSQL).df()

# I. Más consultas sobre una tabla 

# a. Listar los códigos de departamento y  sus nombres, ordenados por estos 
# últimos (sus nombres) de manera descendentes (de la Z a la A). 
# En caso de empate, desempatar por código de departamento de manera ascendente. 

consultaSQL = """
                SELECT id, descripcion
                FROM departamento
                ORDER BY descripcion DESC, id ASC
              """

dataframeResultado = dd.sql(consultaSQL).df()

# b. Listar los registros de la tabla provincia cuyos nombres comiencen 
# con la letra  M. 

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE descripcion LIKE 'M%'
              """

dataframeResultado = dd.sql(consultaSQL).df()

# c. Listar los registros de la tabla provincia cuyos nombres comiencen 
# con la letra S y su quinta letra sea una letra A. 

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE descripcion LIKE 'S___a%'
              """

dataframeResultado = dd.sql(consultaSQL).df()

# d. Listar los registros de la tabla provincia cuyos nombres terminan con 
# la letra A.

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE descripcion LIKE '%a'
              """

dataframeResultado = dd.sql(consultaSQL).df()

# e. Listar los registros de la tabla provincia cuyos nombres tengan 
# exactamente 5 letras. 

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE descripcion LIKE '_____'
              """

dataframeResultado = dd.sql(consultaSQL).df()

# f. Listar los registros de la tabla provincia cuyos nombres tengan ”do” 
# en alguna parte de su nombre. 

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE descripcion LIKE '%do%'
              """

dataframeResultado = dd.sql(consultaSQL).df()

# g. Listar los registros de la tabla provincia cuyos nombres tengan ”do” 
# en alguna parte de su nombre y su código sea menor a 30. 

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE descripcion LIKE '%do%' AND id < 30
              """

dataframeResultado = dd.sql(consultaSQL).df()

# h. Listar los registros de la tabla departamento cuyos nombres tengan 
# ”san” en alguna parte de su nombre. Listar sólo id y descripcion. 
# Utilizar los siguientes alias para las columnas: codigo_depto y nombre_depto,
# respectivamente. El resultado debe estar ordenado por sus nombres de manera 
# descendentes (de la Z a la A). 

consultaSQL = """
                SELECT id AS codigo_depto, descripcion AS nombre_depto
                FROM departamento
                WHERE descripcion LIKE '%San%'
                ORDER BY nombre_depto DESC
              """

dataframeResultado = dd.sql(consultaSQL).df()

# i. Devolver aquellos casos de las provincias cuyo nombre terminen con la 
# letra a y el campo cantidad supere 10. Mostrar: nombre de provincia, 
# nombre de departamento, año, semana epidemiológica, descripción de grupo 
# etario y cantidad. Ordenar el resultado por la cantidad (descendente), 
# luego por el nombre de la provincia (ascendente), nombre del departamento 
# (ascendente), año (ascendente) y la descripción del grupo etario (ascendente). 

consultaSQL = """
                SELECT p.descripcion AS nombre_provincia,
                       d.descripcion AS nombre_depto,
                       c.anio,
                       c.semana_epidemiologica,
                       c.id_grupoetario,
                       c.cantidad
                FROM provincia AS p
                INNER JOIN departamento AS d ON d.id_provincia = p.id
                INNER JOIN casos AS c ON c.id_depto = d.id
                WHERE p.descripcion LIKE '%a' AND c.cantidad > 10
                ORDER BY c.cantidad DESC,
                         p.descripcion ASC,
                         d.descripcion ASC,
                         c.anio ASC,
                         c.id_grupoetario ASC
                """

dataframeResultado = dd.sql(consultaSQL).df()

# Ídem anterior, pero devolver sólo aquellas tuplas que tienen el máximo en 
# el campo cantidad. 

consultaSQL = """
                SELECT p.descripcion AS nombre_provincia,
                       d.descripcion AS nombre_depto,
                       c.anio,
                       c.semana_epidemiologica,
                       c.id_grupoetario,
                       c.cantidad
                FROM provincia AS p
                INNER JOIN departamento AS d ON d.id_provincia = p.id
                INNER JOIN casos AS c ON c.id_depto = d.id
                WHERE p.descripcion LIKE '%a' AND c.cantidad > 10
                AND c.cantidad = (
                      SELECT MAX(cantidad) 
                      FROM casos AS c2 
                      INNER JOIN departamento AS d2 ON c2.id_depto = d2.id
                      INNER JOIN provincia AS p2 ON d2.id_provincia = p2.id
                      WHERE p2.descripcion LIKE '%a'
                )
                ORDER BY c.cantidad DESC,
                         p.descripcion ASC,
                         d.descripcion ASC,
                         c.anio ASC,
                         c.id_grupoetario ASC
                """

dataframeResultado = dd.sql(consultaSQL).df()

#J. Reemplazos

# a. Listar los id y descripción de los departamentos. Estos últimos sin 
# tildes y en orden alfabético.

consultaSQL = """
                SELECT d.id,
                       REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(d.descripcion, 'á', 'a'), 'é', 'e'), 'í', 'i'), 'ó', 'o'), 'ú', 'u'), 'Á', 'A'), 'É', 'E') AS descripcion_sin_tildes
                FROM departamento AS d
                ORDER BY descripcion_sin_tildes ASC
              """

dataframeResultado = dd.sql(consultaSQL).df()

# b. Listar los nombres de provincia en mayúscula, sin tildes y en orden 
# alfabético. 

consultaSQL = """
                SELECT UPPER(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(d.descripcion, 'á', 'a'), 'é', 'e'), 'í', 'i'), 'ó', 'o'), 'ú', 'u'), 'Á', 'A'), 'É', 'E')) AS descripcion_sin_tildes
                FROM departamento AS d
                ORDER BY descripcion_sin_tildes ASC
              """

dataframeResultado = dd.sql(consultaSQL).df()

