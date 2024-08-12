import tkinter as tk
from tkinter import ttk
from consultas import Consultas





class Set_up():

    def __init__(self):

        self.tk = tk.Tk()
        self.ex = Consultas("localhost", "postgres", "0711white", "postgres")


    def config(self):

        self.ex.connect_libreria()
        self.ex.obtener_cursor()

        self.tk.title("BIBLIOTECA")
        self.tk.geometry("1080x720")
        self.tk.resizable(True,True)
        self.frame = ttk.Frame(self.tk, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def new_screen(self):
         
         print("nose")







    def nose(self):

        x= self.ex.view_data("libros")

        self.text_area = tk.Text(self.frame, wrap='word', height= 10, width= 130)
        self.text_area.grid(row = 1, column= 0, pady= 10)

        self.text_area.insert(tk.END, x[0:6] )
        self.text_area.insert(tk.END, "\n" + "\n")

        for i in x[7: ]:

                self.text_area.insert(tk.END, str(i) + "\n")

 
        



        self.tk.mainloop()



run = Set_up()

run.config()
run.nose()



