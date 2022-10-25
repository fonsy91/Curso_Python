#https://www.youtube.com/watch?v=2MaAs7XU2T0&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=21

#PROBAMOS LAS EXCEPCIONES QUE NOS OFRECE PYTHON 

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "operacion erronea"

def divide2():
	try:
		op3 = (float(input("Introduce un numero: ")))
		op4 = (float(input("Introduce un numero: ")))
		print("La division es: "+str(op3/op4))
		print("calculo finalizado")
	except ValueError:
		print("El valor es erroneo")
	except ZeroDivisionError:
		print("division por cero error")
	finally:
		print("funcion finalizada")


def evaluaEdad(edad):
	if edad<0:
		raise TypeError("no se permiten edades negativas")
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "cuidate"


#MAIN********************************************
while True:		
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))	
		break 	
	except ValueError:
		print("Los valores no son correctos")

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("operacion no contemplada")


print("operacion ejecutada. continuacion de ejecucion del programa ")

divide2()

print(evaluaEdad(18))