'''
def area_triangulo(base, altura):
    return(base*altura)/2


#print(area_triangulo(5,7))

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)
print(triangulo2)
'''

#NUnca se puede hacer con condicionales o con for etc...

area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(7,5))

destacar_valor=lambda comision:"¡{}! $".format(comision)
comision_Ana=15585
print(destacar_valor(comision_Ana))