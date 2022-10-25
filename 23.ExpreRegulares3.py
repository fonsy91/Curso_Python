import re

#Expresiones regulares usando rangos 
#Python es sensible a expressiones regulares si quieres que 
#no lo sea en la funcion usas re.IGNORECASE

lista_nombres=['hombres','mujeres','mascotas','camión','camion']
nombres=['Ana','Pedro','Rosa','Sandra','Celia']

for elemento in lista_nombres:
    if re.findall('cami[oó]n',elemento):
        print(elemento)


for elemento in nombres:
    #devuelve los nombres con un rango de entre la o a la t
    if re.findall('[o-t]',elemento):
        print(elemento)


