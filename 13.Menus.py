from tkinter import * 

root=Tk()
'''WINDOWS
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


#establecemos el numero de elementos del menu 
archivoMenu=Menu(barraMenu, tearoff=0)
#lo que despliega Archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")



archivoEdicion=Menu(barraMenu)
archivoHerramientas=Menu(barraMenu)
archivoAyuda=Menu(barraMenu)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

'''


'''MAC
root.title('Test Tk menu on mac Catalina Python 3.7.4 tkinter 8.6')

mymenubar = Frame(root, relief='raised', bd=2)
mymenubar.pack(fill=X)

mymenubutton = Menubutton(mymenubar, text='File', )
mymenubutton.pack(side=LEFT)

mymenu = Menu(mymenubutton, tearoff=0)
mymenubutton['menu'] = mymenu
mymenu.add('command', label='Open') # Add Sub Menu 1

mb2 = Menubutton(mymenubar, text='Edit', )
mb2.pack(side=LEFT)
menudd = Menu(mb2, tearoff=0)
mb2['menu'] = menudd
menudd.add('command', label='Cut') # Add Sub Menu 2

myframe1 = Frame(root, bd=2, relief=SUNKEN)
myframe1.pack(side=LEFT)

'''

root.title("Menu")
mymenubar = Frame(root)
mymenubar.pack(fill=X)

mymenubutton = Menubutton(mymenubar, text='File', )
mymenubutton.pack(side=LEFT)

mymenu = Menu(mymenubutton, tearoff=0)
mymenubutton['menu'] = mymenu
mymenu.add('command', label='Open')

root.mainloop()