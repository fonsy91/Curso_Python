import sqlite3

#Hace falta Saber lenguaje SQL
#vamos a ver MySql y SQlite 

'''
PASOS A SEGUIR PARA CONECTAR CON BASE DE DATOS 
1.abrir-Crear conexion 
2.Crear puntero (ejecutar consultas y manejar los resultados)
3.Ejecutar query(consulta)SQL
4.Manejar los resultados de la query(consulta)
    4.1 insertar, leer, Actualizar, borrar
5.Cerrar puntero
6.Cerrar conexion 

#Para poder ver la tabla descargar este programa 
https://sqlitebrowser.org/dl/

'''
#creamos la conexion y el nombre de la base de datos PASO1
miConexion=sqlite3.connect("PrimeraBase")
#creamos el cursor/puntero
miCursor=miConexion.cursor()

#solo se hace una vez para crearla despues de quita o invalida
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
#cada vez que hacemos un cambio hay que verificar y se usa 
#miConexion.commit()

#COMIENZO VIDEO 2 DE BASE DE DATOS 
#insercion de varios productos a la vez 
'''
variosProductos=[
    ("Camiseta",10,"Deportes"),
    ("Jarron",90,"Céramica"),
    ("Camión",20,"Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)
miConexion.commit()
'''
#consulatr los productos de una tabla 
miCursor.execute("SELECT * FROM PRODUCTOS")
#fetchall muestra toda la base de datos 
variosProductos=miCursor.fetchall()
#print(variosProductos)

for producto in variosProductos:
    #print(producto)
    print("Nombre Articulo: ",producto[0], "Seccion: ",producto[2])


#cerramos base de datos PASO6
miConexion.close()