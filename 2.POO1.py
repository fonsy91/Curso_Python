class Coche():

    '''
    Encapsular: se usa para proteger los atributos de la clase 
    con el encapsulamiento no permites que se cambien los valores
    fuera de la clase solo dentro se encapsula con dos giones bajos 
    antes del atributo precedido del self y el punto (self.__largoChasis=250)
    Si encapsulas debes poner los dos giones fuera tambien cuando quieras
    acceder a los atributos de la clase.Tambien se pueden encapsular los 
    metodos de la misma manera def __chequeo_interno(self): .
    '''
    #Constructor de la clase 
    def __init__(self):
        #propiedades de la clase
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    

    #metodos de la clase
    #self hace referencia a la instancia de la clase como (this)
    #el objeto mi coche se almacena en self
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo= self.__chequeo_interno()
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No arrancamos"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene: ",self.__ruedas," ruedas. Un ancho de ", self.__anchoChasis,
        " y un largo de ",self.__largoChasis)
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina='ok'
        self.aceite='ok'
        self.puertas='cerradas'

        if(self.gasolina=='ok' and self.aceite=='ok' and self.puertas=='cerradas'):
            return True
        else:
            return False

#MAIN*********************

#instanciacion de una clase 
miCoche=Coche()

print(miCoche.arrancar(True))
miCoche.estado()


#creamos un segundo coche 
print("----------A continuacion creamos el segundo coche----------")
miCoche2 =Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()


