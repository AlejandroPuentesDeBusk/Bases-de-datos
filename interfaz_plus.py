import tkinter as tk
from tkinter import ttk
from consultas import Consultas

class Set_up():

    def __init__(self):
        self.tk = tk.Tk()
        self.ex = Consultas("localhost", "postgres", "0711white", "postgres")
        self.datos_ingresados = []  # Lista para almacenar los valores ingresados

    def config(self):
        self.ex.connect_libreria()
        self.ex.obtener_cursor()
        


        self.tk.title("BIBLIOTECA")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.frame = ttk.Frame(self.tk, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def probando(self):
        print("Prueba Exitosa")

    def menu(self):
        # BOTONES
        boton_autores = tk.Button(self.frame, text="Autores", command=self.probando, width=40, height=20, padx=10, pady=10)
        boton_autores.grid(row=0, column=0, padx=10, pady=10)

        boton_cat = tk.Button(self.frame, text="Categorías", command=self.probando, width=40, height=20, padx=10, pady=10)
        boton_cat.grid(row=0, column=1, padx=10, pady=10)

        boton_libros = tk.Button(self.frame, text="Libros", command=self.libros, width=40, height=20, padx=10, pady=10)
        boton_libros.grid(row=0, column=2, padx=10, pady=10)

        boton_editorial = tk.Button(self.frame, text="Editoriales", command=self.probando, width=40, height=20, padx=10, pady=10)
        boton_editorial.grid(row=1, column=0, padx=10, pady=10)

        boton_libreros = tk.Button(self.frame, text="Libreros", command=self.probando, width=40, height=20, padx=10, pady=10)
        boton_libreros.grid(row=1, column=1, padx=10, pady=10)

        boton_usuarios = tk.Button(self.frame, text="Usuarios", command=self.probando, width=40, height=20, padx=10, pady=10)
        boton_usuarios.grid(row=1, column=2, padx=10, pady=10)

        boton_prestamos = tk.Button(self.frame, text="Prestamos", command=self.probando, width=40, height=20, padx=10, pady=10)
        boton_prestamos.grid(row=0, column=3, padx=10, pady=10)

        self.tk.mainloop()

    def show_any(self, tabla, ventana, columnas):
        x = self.ex.view_data(tabla)
        ventana.insert(tk.END, x[0:columnas])
        ventana.insert(tk.END, "\n" + "\n")
        for i in x[columnas + 1:]:
            ventana.insert(tk.END, str(i) + "\n")

    def add_any(self, nombre_t, columnas, valores):
        self.ex.add_data(nombre_t, columnas, valores)
        None

    def cuadro_texto(self, texto, linea, columna, ventana):
        text = tk.Text(ventana, height=1, width=20)
        text.grid(row=linea, column=columna, padx=10, pady=10)
        text.insert(tk.END, texto)

    def cuadro_entrada(self, linea, columna, ventana):
        entrada = tk.Entry(ventana, width=80)
        entrada.grid(row=linea, column=columna, padx=10, pady=10)
        return entrada

    def guardar_todos_los_datos(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        self.datos_ingresados = [
            self.entrada_titulo.get(),
            int(self.entrada_autor.get()),
            int(self.entrada_editorial.get()),
            self.entrada_anio.get(),
            int(self.entrada_categoria.get()),
            int(self.entrada_librero.get())
        ]
        print(f"Datos ingresados: {self.datos_ingresados}")

        valores = self.datos_ingresados

        columnas_libros=["titulo","id_autor","id_editorial","año_publicacion","id_categoria","id_librero"]

        self.ex.add_data("libros",columnas_libros,valores)

    def libros(self):
        # VENTANA
        self.tk.title("LIBROS")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.window_1 = ttk.Frame(self.tk, padding="10")
        self.window_1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cuadro de texto titulo
        self.cuadro_texto("TITULO", 2, 0, self.window_1)
        self.entrada_titulo = self.cuadro_entrada(3, 0, self.window_1)

        # Cuadro de texto autor
        self.cuadro_texto("ID AUTOR", 4, 0, self.window_1)
        self.entrada_autor = self.cuadro_entrada(5, 0, self.window_1)

        self.cuadro_texto("ID EDITORIAL", 6, 0, self.window_1)
        self.entrada_editorial = self.cuadro_entrada(7, 0, self.window_1)

        self.cuadro_texto("AÑO DE PUBLICACION", 8, 0, self.window_1)
        self.entrada_anio = self.cuadro_entrada(9, 0, self.window_1)

        self.cuadro_texto("ID CATEGORIA", 10, 0, self.window_1)
        self.entrada_categoria = self.cuadro_entrada(11, 0, self.window_1)

        self.cuadro_texto("ID LIBRERO", 12, 0, self.window_1)
        self.entrada_librero = self.cuadro_entrada(13, 0, self.window_1)

        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=10, width=100)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER LIBROS
        ver_libros = tk.Button(self.window_1, text="Inventario", command=lambda: self.show_any("libros", self.mostrar, 6), width=10, height=2, padx=10, pady=10)
        ver_libros.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR DATOS
        guardar_datos = tk.Button(self.window_1, text="Guardar Datos", command=self.guardar_todos_los_datos, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=1, padx=10, pady=10)




        
        

        self.tk.mainloop()


run = Set_up()
run.config()
run.menu()
