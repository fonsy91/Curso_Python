import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

'''
miCursor.execute(```
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20)
    )
```)

productos=[
    ("pelota",20,"juguetería"),
    ("pantalon",15,"confeccion"),
    ("destornillador",25,"ferreteria"),
    ("jarron",45,"ceramica"),
]

'''
'''
Si quieres que otro campo sea unico y no se pueda repetir debes añadir 
UNIQUE, puedes gregarla donde quieras  

NOMBRE_ARTICULO VARCHAR(50) UNIQUE,

'''
#ver la informacion almacenada 
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")
productos=miCursor.fetchall()
print(productos)

#actualizacion de registros 
#vamos a cambiar el precio de un articulo 
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota' ")

#borrar un registro 
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")

miConexion.commit()
miConexion.close()