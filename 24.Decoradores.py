
'''
Funciones que a su vez añaden funcionalidades a otra funciones 

'''
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #Acciones adicionales que decoran 
        print("Vamos a realizar un calculo: ")
        funcion_parametro()
        print("Hemos terminado el calculo")

    return funcion_interior

#Hay que poner el @funcion_decoradora encima de la funcion y ya lo hara 
@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)



suma()
resta()


#FINAL DEL CURSO FALTA MIRAR COMO CREAR EJECUTABLES 