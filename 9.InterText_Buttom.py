from tkinter import * 

'''
Todas las opciones de Lable valen para Entry 
grid(row=1, column=2): divide el frame en una cuadricula 
stiky(N): lo coloca arriba, abajo... usa cardinales (N,W,E,S,NE,SE,SW,NW)
pady: hace que no esten muy junto da separaciones entre elementos 
la opcion show="*" es para contraseñas

'''

raiz= Tk()
miFrame= Frame(raiz, width=500, height=500)
miFrame.pack()

miNombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=5, pady=5)
cuadroPass.config(show="*", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=5, pady=5)
cuadroApellido.config(justify="center")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=5, pady=5)
cuadroDireccion.config(justify="center")

nombreLabel= Label(miFrame, text="Nombre: ",font=("Comic Sans MS",15))
nombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

ApellidoLabel= Label(miFrame, text="Apellido: ",font=("Comic Sans MS",15))
ApellidoLabel.grid(row=2, column=0,sticky="w", padx=5, pady=5)

DireccionLabel= Label(miFrame, text="Direccion: ",font=("Comic Sans MS",15))
DireccionLabel.grid(row=3, column=0,sticky="w", padx=5, pady=5)

passLabel = Label(miFrame, text="Password: ",font=("Comic Sans MS",15))
passLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)

#cuadro de texto para comentarios 
comentariosLabel = Label(miFrame, text="Comentarios: ",font=("Comic Sans MS",15))
comentariosLabel.grid(row=4, column=0, sticky="e", padx=5, pady=5)
textComentario= Text(miFrame, width=25, height=5)
textComentario.grid(row=4, column=1, padx=5, pady=5)
scrollvert=Scrollbar(miFrame, command=textComentario.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")
textComentario.config(yscrollcommand=scrollvert.set)

def codigoBoton():
    miNombre.set("Alfonso")


#agregamos boton 
botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()






raiz.mainloop()
