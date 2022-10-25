from tkinter import * 
from tkinter import messagebox
import sqlite3


#FUNCIONES---------------- 

def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
        ''')
    
        messagebox.showinfo("BBDD","BBDD creada con exito")

    except:
        messagebox.showwarning("¡Atencion!","La BBDD ya existe")


def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Desea salir de la aplicacion?")
    if(valor=="yes"):
        root.destroy()


def limpiarCampos():
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0, END)
    #desde el principio hasta el final 


def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    '''
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+miNombre.get()+
    "','"+miPass.get()+
    "','"+miApellido.get()+
    "','"+miDireccion.get()+
    "','"+textoComentario.get("1.0",END)+"')")
    '''

    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(), textoComentario.get("1.0",END)
    #onsulta parametrizada 
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))


    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")


def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+miID.get())
    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0,usuario[5])


    miConexion.commit()


def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+
    "', PASSWORD='"+miPass.get()+
    "', APELLIDO='"+miApellido.get()+
    "', DIRECCION='"+miDireccion.get()+
    "', COMENTARIOS='"+textoComentario.get("1.0", END)+
    "' WHERE ID="+miID.get())

    miConexion.commit()
    messagebox.showinfo("BBDD","Registro Actualizado con exito")


def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+miID.get())
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro borrado con exito")



#----------------------------------------------

root=Tk()
root.title("Aplicacion BBDD")

#https://www.youtube.com/watch?v=o8E869dmK3U&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=60

barraMenu= Frame(root)
barraMenu.pack()

#Boton de barra de menu Conectar---------------- 
botonConectar=Menubutton(barraMenu, text="BBDD")
botonConectar.grid(row=0,column=0)
miMenu=Menu(botonConectar, tearoff=0)
botonConectar['menu']=miMenu
miMenu.add('command', label="Conectar", command=conexionBBDD)
miMenu.add('command', label="Salir", command=salirAplicacion)
#----------------------------------------------

#Boton de barra de menu Borrar---------------- 
botonBorrar=Menubutton(barraMenu, text="Borrar")
botonBorrar.grid(row=0,column=1)
miMenu1=Menu(botonBorrar, tearoff=0)
botonBorrar['menu']=miMenu1
miMenu1.add('command', label="Borrar campos", command=limpiarCampos)
#----------------------------------------------

#Boton de barra de menu CRUD---------------- 
botonCRUD=Menubutton(barraMenu, text="CRUD")
botonCRUD.grid(row=0,column=2)
miMenu2=Menu(botonCRUD, tearoff=0)
botonCRUD['menu']=miMenu2
miMenu2.add('command', label="Crear", command=crear)
miMenu2.add('command', label="Leer", command=leer)
miMenu2.add('command', label="Actualizar", command=actualizar)
miMenu2.add('command', label="Borrar", command=eliminar)
#----------------------------------------------

#Boton de barra de menu Ayuda---------------- 
botonAyuda=Menubutton(barraMenu, text="Ayuda")
botonAyuda.grid(row=0,column=3)
miMenu3=Menu(botonAyuda, tearoff=0)
botonAyuda['menu']=miMenu3
miMenu3.add('command', label="Licencia")
miMenu3.add('command', label="Acerca de...")
#----------------------------------------------


#COMIENZO DE ENTRYS---------------------------

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()


cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(bg="#F5F4F1", justify="center")

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(bg="#F5F4F1", justify="center")


cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(justify="center", show="*", bg="#F5F4F1")


cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
cuadroApellido.config(bg="#F5F4F1", justify="center")

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)
cuadroDireccion.config(bg="#F5F4F1", justify="center")

textoComentario=Text(miFrame, width=26, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert, bg="#F5F4F1")

#COMIENZO DE LABELS---------------------------

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccón:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


#COMIENZO DE BOTONES---------------------------
miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()