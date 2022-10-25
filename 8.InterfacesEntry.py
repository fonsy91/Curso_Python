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


cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=5, pady=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=5, pady=5)



nombreLabel= Label(miFrame, text="Nombre: ",font=("Comic Sans MS",15))
nombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

ApellidoLabel= Label(miFrame, text="Apellido: ",font=("Comic Sans MS",15))
ApellidoLabel.grid(row=1, column=0,sticky="w", padx=5, pady=5)

DireccionLabel= Label(miFrame, text="Direccion: ",font=("Comic Sans MS",15))
DireccionLabel.grid(row=2, column=0,sticky="w", padx=5, pady=5)



raiz.mainloop()
