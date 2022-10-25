from tkinter import * 

'''
variableLable = Label(contenedor,opciones)
place(): puedes ubicar el texto en cualquier lugar de
la interface grafica 

fg: da color
'''

root = Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miLabel = Label(miFrame,text="Hola Alfonso")
miLabel.place(x=100, y=200)
#otra forma 
Label(miFrame, text="otro texto", fg="red", font=("Comic Sans MS",18)).place(x=50, y=50)

#si quieres poner una foto 
#miImagen = PhotoImage(file="ruta/nombre de imagen")
#Label(miFrame,image=miImagen).place(x=100,y=100)

root.mainloop()

