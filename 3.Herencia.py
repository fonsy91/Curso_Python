#SUPERCLASE, clase padre 
class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenado: ",self.frena)


#clase furgoneta
class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


#Nuestra clase moto hereda de vehiculos
class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenado: ",self.frena,
        "\n",self.hcaballito)

#clase VElectrico no hereda de nadie 
class VElectricos():

    def __init__(self):
        self.autonomia=100

    def CargarEnergia(self):
        self.cargando=True

'''
tiene atributos de la clase veiculos y de la clase Velectricos 
de hay la herencia multiple. Cuando hay herencia multiple se le 
da preferencia a la primera clase que indiques 
super(): donde la coloques va a llamar al metodo de la clase padre 
isistance(): devuelve si un objeto pertenece a una clase: 
isistance(Manuel, Empleado)
'''
class BicicletaElectrica(VElectricos,Vehiculos):
    pass

#MAIN********************************
miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici = BicicletaElectrica()