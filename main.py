import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import win32print
import win32api
import os
import time
import data

class MyGUI:
    def __init__(self):
        self.app = Tk()
        self.app.title('Recibo')

        label01 = Label(self.app, text = "Matrícula", font= ('Helvetica 12'), width = 10).grid(row = 0, column = 0, sticky = W, padx = 5, pady = 5)


        self.input01 = Entry(self.app)
        self.input01.grid(row = 0, column = 1, sticky = W, padx = 5, pady = 5)

        button02 = Button(self.app, text = "Limpar", width = 10, command = self.Clear).grid(row = 0, column = 2, sticky = W, padx = 5, pady = 5)

        self.listbox = Listbox(self.app)

        button01 = Button(self.app, text = "Buscar", width = 10, command = self.GetMat).grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

        button02 = Button(self.app, text = "Imprimir", width =17, command = self.Print_data).grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

        button03 = Button(self.app, text = "Sair", width = 10, command = self.app.destroy).grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

        self.app.mainloop()

    def GetMat(self):
        getmat = self.input01.get()
        recibo = data.Recibo(getmat)
        self.result = recibo.buscar_dados()

        self.listbox.insert(0, self.result['PACIENTE'])
        self.listbox.insert(1, self.result['MATSAME'])
        self.listbox.insert(2, self.result['ARMARIO'])
        self.listbox.insert(3, self.result['SALA'])
        self.listbox.insert(4, self.result['LINHA'])
        self.listbox.insert(5, self.result['COLUNA'])
        self.listbox.grid(row = 1, columnspan = 3, sticky = EW, padx = 15, pady = 15)

    def Print_data(self):
        getmat = self.input01.get()
        recibo = data.Recibo(getmat)
        self.result = recibo.buscar_dados()
        path_file = r"C:\app_same\results"
        folder_file = os.listdir(path_file)

        file = open((path_file + r'\file.txt'), "w")
        file.write("{:^42}".format(self.result['TITULO'][0]))
        file.write("\n")
        file.write("{:^10}".format(self.result['PACIENTE'][0] + "\n"))
        file.write("{:<}".format(self.result['MATSAME'][0] + "\n"))
        file.write("{:<}".format(self.result['ARMARIO'][0] + "\n"))
        file.write("{:<}".format(self.result['LINHA'][0] + " " + self.result['COLUNA'][0]))
        file.close()
        
        for f in folder_file:
            win32api.ShellExecute(0, "print", f, None, path_file, 0)
        self.Clear()

    def Clear(self):
        self.input01.delete(0, "end")
        self.listbox.destroy()
        self.listbox = Listbox(self.app)

MyGUI()