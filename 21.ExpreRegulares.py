import re


cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

#busca aprender en cadena
print(re.search("aprender",cadena))

textoBuscar="expresiones"
if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

textoBuscar2="regulares"
#si no la encuentra devuelve None 
textoEncontrado=re.search(textoBuscar2, cadena)
#El metodo start devuelve en que posicion donde comienza
print(textoEncontrado.start())
#El metodo end devuelve en que posicion acaba 
print(textoEncontrado.end())
#El metodo span devuelve las dos anteriores en una lista
print(textoEncontrado.span())

textoBuscar3="Python"
#devuelve el numero de veces que se repite una palabra 
print(re.findall(textoBuscar3,cadena))
print(len(re.findall(textoBuscar3,cadena)))
