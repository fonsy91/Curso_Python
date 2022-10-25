from tkinter import * 

#https://docs.python.org/3.3/library/tk.html

raiz=Tk()

raiz.title("Ventana de pruebas")
#ancho o alto (no permititmos redimensionar)
#raiz.resizable(0,0) 
#raiz.iconbitmap("ruta"), cambias el icono de la ventana

#dimensiones de la ventana 
#raiz.geometry("500x500")
raiz.config(bg="blue")

#creamos el frame 
miFrame = Frame()
#ahora lo empaquetamos es decir lo metemos en la raiz 
miFrame.pack(side="left", anchor="s")

#damos color y tamaño al frame para verlo
miFrame.config(bg="red")
miFrame.config(width="650", height="350")

#cambiamos las caracteristicas del borde
miFrame.config(bd=10)
miFrame.config(relief="raised")

#cambiar cursor 
miFrame.config(cursor="pirate")


#bucle infinito hasta que se cierre el programa 
raiz.mainloop()
