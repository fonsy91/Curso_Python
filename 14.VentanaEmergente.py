from tkinter import * 
from tkinter import messagebox

root=Tk()


#ventanas emergentes 
#acerca de
def infoAdicional():
    messagebox.showinfo("Procesador de Alfonso","Procesador de textos 2020")
#licencia
def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU ")
#Salir
def salirAplicacion():
    valor= messagebox.askquestion("salir","Desea salir de la aplicacion?")
    #valor= messagebox.askokcancel("salir","Desea salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
#cerrar
def cerrarDocumento():
    valor= messagebox.askretrycancel("Reintentar","No es posible cerrar")
    if valor=="False":
        root.destroy()


'''
root.title("Menu")
root.config(width=300, height=300)

mymenubar = Frame(root)
mymenubar.pack(fill=X)

mymenubutton = Menubutton(mymenubar, text='Archivo', )
mymenubutton.pack(side=LEFT)

mymenu = Menu(mymenubutton, tearoff=0)
mymenubutton['menu'] = mymenu
mymenu.add('command', label='Open')
'''
root.title("Menu")
root.geometry('340x340')


mymenubar = Frame(root)
#mymenubar.pack(fill=X)
mymenubar.pack()

#Boton de menu Archivo------------------------------
menuArchivo = Menubutton(mymenubar, text='Archivo')
menuArchivo.grid(row=0,column=0)

miMenu=Menu(menuArchivo, tearoff=0)
menuArchivo['menu']=miMenu
miMenu.add('command', label="Nuevo")
miMenu.add('command', label="Guardar", command=cerrarDocumento)
miMenu.add('command', label="Guardar Como")
miMenu.add_separator()
miMenu.add('command', label="Cerrar")
miMenu.add('command', label="Salir", command=salirAplicacion)
#----------------------------------------------------


#Boton de menu Edicion------------------------------
menuEdicion = Menubutton(mymenubar, text='Edicion')
menuEdicion.grid(row=0,column=1)

miMenu2=Menu(menuEdicion, tearoff=0)
menuEdicion['menu']=miMenu2
miMenu2.add('command', label="Copiar")
miMenu2.add('command', label="Cortar")
miMenu2.add('command', label="Pegar")

#----------------------------------------------------

#Boton de menu Herramientas------------------------------
menuHerramientas = Menubutton(mymenubar, text='Herramientas')
menuHerramientas.grid(row=0,column=2)

#----------------------------------------------------

#Boton de menu Ayuda------------------------------
menuAyuda = Menubutton(mymenubar, text='Ayuda')
menuAyuda.grid(row=0,column=3)

miMenu3=Menu(menuAyuda, tearoff=0)
menuAyuda['menu']=miMenu3
miMenu3.add('command', label="Licencia", command=avisoLicencia)
miMenu3.add('command', label="Acerca de..", command=infoAdicional)
#----------------------------------------------------





root.mainloop()