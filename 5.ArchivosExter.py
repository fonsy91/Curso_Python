from io import open
'''

#creamos un archivo externo modo escritura 
archivo_texto=open("archivo.txt","w")

frase="Estupendo dia para estudiar python \n el miercoles"

#incluimos la variable en el archivo 
archivo_texto.write(frase)

#cerramos el archivo en memoria 
archivo_texto.close()

'''
'''
#modo lectura de archivos 
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
#pinta lo que hay guardado en el archivo 
print(texto)

#hay otro metodo readlines(): lee linea a linea y lo almacena en una lista

'''

'''
#modo lectura con readlines 
archivo_texto=open("archivo.txt","r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
'''

#abre el archivo en modo agregar 
archivo_texto=open("archivo.txt","a")
archivo_texto.write("\n siempre es una buena ocasion para estudiar")
archivo_texto.close()

'''
con seek(): colocas el puntero donde quieras del archivo
para poder leer desde donde quieras archivo_texto.seek(11)
colocas dentro la posicion 

'''