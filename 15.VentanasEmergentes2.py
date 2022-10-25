#Ventanas emergentes de archivos 
from tkinter import * 
from tkinter import filedialog

root =Tk()

def abreFichero():
    fichero= filedialog.askopenfilename(title="Abrir")
    print(fichero)
    #opcion: initialdir="C:"
    #opcion: filetypes=((tupla))


#------------------------
Button(root, text="Abrir fichero", command=abreFichero).pack()


root.mainloop()
