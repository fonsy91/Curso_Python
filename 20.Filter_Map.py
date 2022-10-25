
'''
Verfifica que los elementos de una secuencia cumplen una condicion,
devolviendo un iterador con elementos que cumplen dicha condicion 
Normalmente se usa con listas de objetos 
'''
'''
#detectar que numeros son pares y cuales no y que me devuelva los pares
def numero_par(num):
    if num % 2 == 0:
        return True


numeros=[17,24,7,39,8,51,92]

#print(list(filter(numero_par,numeros)))

#podemos usar funcion lambda
print(list(filter(lambda numero_par:numero_par%2==0, numeros)))

'''

class Empleado:

    #constructor
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario


    def __str__(self):
        return "{} que trabaja como {} tiene un salrio de {} $".format(self.nombre, self.cargo, self.salario)



listaEmpleados=[
    Empleado("Juan","Director",75000),
    Empleado("Ana","Presidenta",85000),
    Empleado("Antonio","Administrativo",25000),
    Empleado("Sara","Secretaria",27000),
    Empleado("Mario","Botones",21000),
]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleados_salario in salarios_altos:
    print(empleados_salario)

'''
Map
Aplica una funcion a cada elemento de una lista iterable
(listas,tuplas etc) devolviendo una lista con los resultados 
'''

listaEmpleados2=[
    Empleado("Juan","Director",6700),
    Empleado("Ana","Presidenta",7500),
    Empleado("Antonio","Administrativo",2100),
    Empleado("Sara","Secretaria",2150),
    Empleado("Mario","Botones",1800),
]

def calculo_comision(empleado):
    if(empleado.salario<=3000):
        empleado.salario=empleado.salario*1.03
        
    return empleado

#a cada elemento de la lista realizara la funcion 
listaEmpleComision=map(calculo_comision,listaEmpleados2)

for empleado in listaEmpleComision:
    print(empleado)