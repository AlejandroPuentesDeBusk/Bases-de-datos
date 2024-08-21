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

        self.config()
        # BOTONES
        boton_autores = tk.Button(self.frame, text="Autores", command=self.autores, width=40, height=20, padx=10, pady=10)
        boton_autores.grid(row=0, column=0, padx=10, pady=10)

        boton_cat = tk.Button(self.frame, text="Categorías", command=self.categorias, width=40, height=20, padx=10, pady=10)
        boton_cat.grid(row=0, column=1, padx=10, pady=10)

        boton_libros = tk.Button(self.frame, text="Libros", command=self.libros, width=40, height=20, padx=10, pady=10)
        boton_libros.grid(row=0, column=2, padx=10, pady=10)

        boton_editorial = tk.Button(self.frame, text="Editoriales", command=self.editoriales, width=40, height=20, padx=10, pady=10)
        boton_editorial.grid(row=1, column=0, padx=10, pady=10)

        boton_libreros = tk.Button(self.frame, text="Libreros", command=self.libreros, width=40, height=20, padx=10, pady=10)
        boton_libreros.grid(row=1, column=1, padx=10, pady=10)

        boton_usuarios = tk.Button(self.frame, text="Usuarios", command=self.usuarios, width=40, height=20, padx=10, pady=10)
        boton_usuarios.grid(row=1, column=2, padx=10, pady=10)

        boton_prestamos = tk.Button(self.frame, text="Prestamos", command=self.prestamos, width=40, height=20, padx=10, pady=10)
        boton_prestamos.grid(row=0, column=3, padx=10, pady=10)

        self.tk.mainloop()

    def show_any(self, tabla, ventana, columnas):
        x = self.ex.view_data(tabla)
        ventana.insert(tk.END, x[0:columnas+1])
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

    def guardar_todos_los_datos_libros(self):

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


    def eliminar_libros(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        eliminar= int(self.entrada_id_libro.get())
        print(f"Eliminar ID: {eliminar}")


        columna="id_libro"

        self.ex.del_data("libros",columna,eliminar)


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


        self.cuadro_texto("ID LIBRO", 5, 2, self.window_1)
        self.entrada_id_libro = self.cuadro_entrada(6, 2, self.window_1)



        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=10, width=100)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER LIBROS
        ver_libros = tk.Button(self.window_1, text="Inventario", command=lambda: self.show_any("libros", self.mostrar, 6), width=10, height=2, padx=10, pady=10)
        ver_libros.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR DATOS
        guardar_datos = tk.Button(self.window_1, text="Guardar Datos", command=self.guardar_todos_los_datos_libros, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=1, padx=10, pady=10)


        # BOTON ELIMINAR DATOS###############################################3
        guardar_datos = tk.Button(self.window_1, text="Eliminar Libro", command=self.eliminar_libros, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=2, padx=10, pady=10)

        #BOTON REGRESAR

        back = tk.Button(self.window_1, text="Regresar", command= self.menu, width=10, height=2, padx=10, pady=10)
        back.grid(row=0, column=2, padx=10, pady=10)



        self.tk.mainloop()


    def guardar_autores(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        self.datos_ingresados = [
            self.entrada_nombre.get(),
            self.entrada_paterno.get(),
            self.entrada_nacionalidad.get(),
            self.entrada_fecha.get(),
        ]
        print(f"Datos ingresados: {self.datos_ingresados}")

        valores = self.datos_ingresados

        columnas_autores=["nombre","apellido_paterno","nacionalidad","fecha_nacimiento"]

        try:

            self.ex.add_data("autores",columnas_autores,valores)

        except Exception as e:

            print("You gave incorrect or incomplete data")


    def eliminar_autor(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        eliminar= int(self.entrada_id_autor.get())
        print(f"Eliminar ID: {eliminar}")


        columna="id_autor"

        self.ex.del_data("autores",columna,eliminar)



    def autores(self):
        # VENTANA
        self.tk.title("LIBROS")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.window_1 = ttk.Frame(self.tk, padding="10")
        self.window_1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cuadro de texto titulo
        self.cuadro_texto("NOMBRE", 2, 0, self.window_1)
        self.entrada_nombre = self.cuadro_entrada(3, 0, self.window_1)

        # Cuadro de texto autor
        self.cuadro_texto("APELLIDO PARTERNO", 4, 0, self.window_1)
        self.entrada_paterno = self.cuadro_entrada(5, 0, self.window_1)

        self.cuadro_texto("NACIONALIDAD", 6, 0, self.window_1)
        self.entrada_nacionalidad = self.cuadro_entrada(7, 0, self.window_1)

        self.cuadro_texto("FECHA DE NACIMIENTO (format: YYYY-MM-DD)", 8, 0, self.window_1)
        self.entrada_fecha = self.cuadro_entrada(9, 0, self.window_1)


        self.cuadro_texto("ID AUTOR", 5, 2, self.window_1)
        self.entrada_id_autor = self.cuadro_entrada(6, 2, self.window_1)


        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=10, width=100)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER AUTORES
        ver_autores = tk.Button(self.window_1, text="Autores", command=lambda: self.show_any("autores", self.mostrar, 4), width=10, height=2, padx=10, pady=10)
        ver_autores.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR AUTORES
        guardar_autores = tk.Button(self.window_1, text="Añadir Autor", command=self.guardar_autores, width=15, height=2, padx=10, pady=10)
        guardar_autores.grid(row=3, column=1, padx=10, pady=10)


        # BOTON ELIMINAR DATOS###############################################3
        guardar_datos = tk.Button(self.window_1, text="Eliminar Autor", command=self.eliminar_autor, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=2, padx=10, pady=10)

        #BOTON REGRESAR

        back = tk.Button(self.window_1, text="Regresar", command= self.menu, width=10, height=2, padx=10, pady=10)
        back.grid(row=0, column=2, padx=10, pady=10)



        self.tk.mainloop()



    def guardar_categorias(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        self.datos_ingresados = [
            self.entrada_nombre.get(),
            self.entrada_descripcion.get(),
            self.entrada_fecha_c.get(),
            int(self.entrada_num_l.get()),
        ]
        print(f"Datos ingresados: {self.datos_ingresados}")

        valores = self.datos_ingresados

        columnas_categoria=["nombre","descripcion","fecha_creacion","numero_libros"]

        self.ex.add_data("categorias",columnas_categoria,valores)


    def eliminar_categoria(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        eliminar= int(self.entrada_id_categoria.get())
        print(f"Eliminar ID: {eliminar}")


        columna="id_categoria"

        self.ex.del_data("categorias",columna,eliminar)




    def categorias(self):
        # VENTANA
        self.tk.title("CATEGORIAS")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.window_1 = ttk.Frame(self.tk, padding="10")
        self.window_1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cuadro de texto titulo
        self.cuadro_texto("NOMBRE", 2, 0, self.window_1)
        self.entrada_nombre = self.cuadro_entrada(3, 0, self.window_1)

        # Cuadro de texto autor
        self.cuadro_texto("DESCRIPCION", 4, 0, self.window_1)
        self.entrada_descripcion = self.cuadro_entrada(5, 0, self.window_1)

        self.cuadro_texto("FECHA DE CREACION", 6, 0, self.window_1)
        self.entrada_fecha_c = self.cuadro_entrada(7, 0, self.window_1)

        self.cuadro_texto("NUMERO LIBROS", 8, 0, self.window_1)
        self.entrada_num_l = self.cuadro_entrada(9, 0, self.window_1)


        self.cuadro_texto("ID CATEGORIA", 5, 2, self.window_1)
        self.entrada_id_categoria = self.cuadro_entrada(6, 2, self.window_1)



        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=10, width=110)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER CATEGORIAS
        ver_categorias = tk.Button(self.window_1, text="Categorias", command=lambda: self.show_any("categorias", self.mostrar, 4), width=10, height=2, padx=10, pady=10)
        ver_categorias.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR CATEGORIAS
        guardar_categorias = tk.Button(self.window_1, text="Añadir Categoria", command=self.guardar_categorias, width=15, height=2, padx=10, pady=10)
        guardar_categorias.grid(row=3, column=1, padx=10, pady=10)


        # BOTON ELIMINAR DATOS###############################################3
        guardar_datos = tk.Button(self.window_1, text="Eliminar Categoria", command=self.eliminar_categoria, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=2, padx=10, pady=10)

        #BOTON REGRESAR

        back = tk.Button(self.window_1, text="Regresar", command= self.menu, width=10, height=2, padx=10, pady=10)
        back.grid(row=0, column=2, padx=10, pady=10)



        self.tk.mainloop()




    def guardar_editorial(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        self.datos_ingresados = [
            self.entrada_nombre.get(),
            int(self.entrada_telefono.get()),
            self.entrada_correo.get(),
        ]
        print(f"Datos ingresados: {self.datos_ingresados}")

        valores = self.datos_ingresados

        columnas_editorial=["nombre","telefono","correo_electronico"]

        self.ex.add_data("editoriales",columnas_editorial,valores)


    def eliminar_editorial(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        eliminar= int(self.entrada_id_editorail.get())
        print(f"Eliminar ID: {eliminar}")


        columna="id_editorial"

        self.ex.del_data("editoriales",columna,eliminar)


    def editoriales(self):
        # VENTANA
        self.tk.title("EDITORIALES")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.window_1 = ttk.Frame(self.tk, padding="10")
        self.window_1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cuadro de texto titulo
        self.cuadro_texto("NOMBRE", 2, 0, self.window_1)
        self.entrada_nombre = self.cuadro_entrada(3, 0, self.window_1)

        # Cuadro de texto autor
        self.cuadro_texto("TELEFONO", 4, 0, self.window_1)
        self.entrada_telefono = self.cuadro_entrada(5, 0, self.window_1)

        self.cuadro_texto("CORREO ELECTRÓNICO", 6, 0, self.window_1)
        self.entrada_correo = self.cuadro_entrada(7, 0, self.window_1)




        self.cuadro_texto("ID EDITORIAL", 5, 2, self.window_1)
        self.entrada_id_editorail = self.cuadro_entrada(6, 2, self.window_1)



        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=10, width=110)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER EDITORIALES
        ver_editorial = tk.Button(self.window_1, text="Editoriales", command=lambda: self.show_any("editoriales", self.mostrar, 3), width=10, height=2, padx=10, pady=10)
        ver_editorial.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR EDITORIALES
        guardar_editoriales = tk.Button(self.window_1, text="Añadir Editorial", command=self.guardar_editorial, width=15, height=2, padx=10, pady=10)
        guardar_editoriales.grid(row=3, column=1, padx=10, pady=10)


        # BOTON ELIMINAR DATOS###############################################3
        guardar_datos = tk.Button(self.window_1, text="Eliminar Editorial", command=self.eliminar_editorial, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=2, padx=10, pady=10)

        #BOTON REGRESAR

        back = tk.Button(self.window_1, text="Regresar", command= self.menu, width=10, height=2, padx=10, pady=10)
        back.grid(row=0, column=2, padx=10, pady=10)



        self.tk.mainloop()



    def guardar_usuarios(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        self.datos_ingresados = [
            self.entrada_nombre.get(),
            self.entrada_apelliedo_p_u.get(),
            self.entrada_apelliedo_m_u.get(),
            int(self.entrada_telefono_u.get()),
            self.entrada_direccion.get(),
            self.entrada_correo_u.get(),
            self.entrada_fecha_r.get(),

        ]
        print(f"Datos ingresados: {self.datos_ingresados}")

        valores = self.datos_ingresados

        columnas_usuarios=["nombre","apellido_paterno","apellido_materno","telefono","direccion","correo_electronico","fecha_registro"]

        self.ex.add_data("usuarios",columnas_usuarios,valores)


    def eliminar_usuario(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        eliminar= int(self.entrada_id_usuario.get())
        print(f"Eliminar ID: {eliminar}")


        columna="id_usuario"

        self.ex.del_data("usuarios",columna,eliminar)


    def usuarios(self):
        # VENTANA
        self.tk.title("USUARIOS")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.window_1 = ttk.Frame(self.tk, padding="10")
        self.window_1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cuadro de texto titulo
        self.cuadro_texto("NOMBRE", 2, 0, self.window_1)
        self.entrada_nombre = self.cuadro_entrada(3, 0, self.window_1)

        # Cuadro de texto autor
        self.cuadro_texto("APELLIDO PATERNO", 4, 0, self.window_1)
        self.entrada_apelliedo_p_u= self.cuadro_entrada(5, 0, self.window_1)

        self.cuadro_texto("APELLIDO MATERNO", 6, 0, self.window_1)
        self.entrada_apelliedo_m_u = self.cuadro_entrada(7, 0, self.window_1)

        self.cuadro_texto("TELEFONO", 8, 0, self.window_1)
        self.entrada_telefono_u = self.cuadro_entrada(9, 0, self.window_1)

        self.cuadro_texto("DIRECCION", 10, 0, self.window_1)
        self.entrada_direccion = self.cuadro_entrada(11, 0, self.window_1)

        self.cuadro_texto("CORREO ELECTRONICO", 12, 0, self.window_1)
        self.entrada_correo_u = self.cuadro_entrada(13, 0, self.window_1)

        self.cuadro_texto("FECHA DE REGISTRO", 14, 0, self.window_1)
        self.entrada_fecha_r = self.cuadro_entrada(15, 0, self.window_1)

        self.cuadro_texto("ID USUARIO", 6, 2, self.window_1)
        self.entrada_id_usuario = self.cuadro_entrada(7, 2, self.window_1)



        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=5, width=120)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER CATEGORIAS
        ver_usuario = tk.Button(self.window_1, text="Usuarios", command=lambda: self.show_any("usuarios", self.mostrar, 7), width=10, height=2, padx=10, pady=10)
        ver_usuario.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR CATEGORIAS
        guardar_ususarios = tk.Button(self.window_1, text="Añadir Usuario", command=self.guardar_usuarios, width=15, height=2, padx=10, pady=10)
        guardar_ususarios.grid(row=3, column=1, padx=10, pady=10)


        # BOTON ELIMINAR DATOS###############################################3
        guardar_datos = tk.Button(self.window_1, text="Eliminar Usuario", command=self.eliminar_usuario, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=2, padx=10, pady=10)

        #BOTON REGRESAR

        back = tk.Button(self.window_1, text="Regresar", command= self.menu, width=10, height=2, padx=10, pady=10)
        back.grid(row=0, column=2, padx=10, pady=10)



        self.tk.mainloop()





    def guardar_prestamo(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        self.datos_ingresados = [
            int(self.entrada_id_usuario_p.get()),
            int(self.entrada_id_libro_p.get()),
            self.entrada_fecha_p.get(),
            self.entrada_fecha_d.get()
 
        ]
        print(f"Datos ingresados: {self.datos_ingresados}")

        valores = self.datos_ingresados

        columnas_prestamos=["id_usuario","id_libro","fecha_prestamo","fecha_devolucion"]

        self.ex.add_data("prestamos",columnas_prestamos,valores)


    def eliminar_prestamo(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        eliminar= int(self.entrada_id_prestamo.get())
        print(f"Eliminar ID: {eliminar}")


        columna="id_prestamo"

        self.ex.del_data("prestamos",columna,eliminar)


    def prestamos(self):
        # VENTANA
        self.tk.title("PRESTAMOS")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.window_1 = ttk.Frame(self.tk, padding="10")
        self.window_1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cuadro de texto titulo
        self.cuadro_texto("ID USUSARIO", 2, 0, self.window_1)
        self.entrada_id_usuario_p = self.cuadro_entrada(3, 0, self.window_1)

        # Cuadro de texto autor
        self.cuadro_texto("ID LIBRO", 4, 0, self.window_1)
        self.entrada_id_libro_p= self.cuadro_entrada(5, 0, self.window_1)

        self.cuadro_texto("FECHA DE PRESTAMOS", 6, 0, self.window_1)
        self.entrada_fecha_p = self.cuadro_entrada(7, 0, self.window_1)

        self.cuadro_texto("FECHA DE DEVOLUCION", 8, 0, self.window_1)
        self.entrada_fecha_d = self.cuadro_entrada(9, 0, self.window_1)


        self.cuadro_texto("ID PRESTAMO", 6, 2, self.window_1)
        self.entrada_id_prestamo = self.cuadro_entrada(7, 2, self.window_1)



        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=20, width=100)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER CATEGORIAS
        ver_prestamo = tk.Button(self.window_1, text="Prestamos", command=lambda: self.show_any("prestamos", self.mostrar, 4), width=10, height=2, padx=10, pady=10)
        ver_prestamo.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR CATEGORIAS
        guardar_prestamos = tk.Button(self.window_1, text="Registar Presmano", command=self.guardar_prestamo, width=15, height=2, padx=10, pady=10)
        guardar_prestamos.grid(row=3, column=1, padx=10, pady=10)


        # BOTON ELIMINAR DATOS###############################################3
        guardar_datos = tk.Button(self.window_1, text="Eliminar Prestamo", command=self.eliminar_prestamo, width=15, height=2, padx=10, pady=10)
        guardar_datos.grid(row=3, column=2, padx=10, pady=10)

        #BOTON REGRESAR

        back = tk.Button(self.window_1, text="Regresar", command= self.menu, width=10, height=2, padx=10, pady=10)
        back.grid(row=0, column=2, padx=10, pady=10)



        self.tk.mainloop()


    def guardar_librero(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        self.datos_ingresados = [
            self.entrada_ubicacion.get(),
            self.entrada_id_categoria_l.get(),
 
        ]
        print(f"Datos ingresados: {self.datos_ingresados}")

        valores = self.datos_ingresados

        columnas_libreros=["ubicacion","id_categoria"]

        self.ex.add_data("libreros",columnas_libreros,valores)


    def eliminar_librero(self):

        # Recopilar los valores de todas las entradas y almacenarlos en la lista
        eliminar= int(self.entrada_id_librero.get())
        print(f"Eliminar ID: {eliminar}")


        columna="id_librero"

        self.ex.del_data("libreros",columna,eliminar)


    def libreros(self):
        # VENTANA
        self.tk.title("PRESTAMOS")
        self.tk.geometry("1490x900")
        self.tk.resizable(True, True)
        self.window_1 = ttk.Frame(self.tk, padding="10")
        self.window_1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Cuadro de texto titulo
        self.cuadro_texto("UBICACION", 2, 0, self.window_1)
        self.entrada_ubicacion = self.cuadro_entrada(3, 0, self.window_1)

        # Cuadro de texto autor
        self.cuadro_texto("ID CATEGORIA", 4, 0, self.window_1)
        self.entrada_id_categoria_l= self.cuadro_entrada(5, 0, self.window_1)


        self.cuadro_texto("ID LIBRERO", 6, 2, self.window_1)
        self.entrada_id_librero = self.cuadro_entrada(7, 2, self.window_1)



        # PANTALLA DE TEXTO
        self.mostrar = tk.Text(self.window_1, wrap='word', height=20, width=100)
        self.mostrar.grid(row=1, column=0, pady=10)

        # BOTON VER CATEGORIAS
        ver_librero = tk.Button(self.window_1, text="Libreros", command=lambda: self.show_any("libreros", self.mostrar, 2), width=10, height=2, padx=10, pady=10)
        ver_librero.grid(row=0, column=0, padx=10, pady=10)

        # BOTON GUARDAR CATEGORIAS
        guardar_librero = tk.Button(self.window_1, text="Registar Presmano", command=self.guardar_librero, width=15, height=2, padx=10, pady=10)
        guardar_librero.grid(row=3, column=1, padx=10, pady=10)


        # BOTON ELIMINAR DATOS###############################################3
        eliminar_librero = tk.Button(self.window_1, text="Eliminar Librero", command=self.eliminar_librero, width=15, height=2, padx=10, pady=10)
        eliminar_librero.grid(row=3, column=2, padx=10, pady=10)

        #BOTON REGRESAR

        back = tk.Button(self.window_1, text="Regresar", command= self.menu, width=10, height=2, padx=10, pady=10)
        back.grid(row=0, column=2, padx=10, pady=10)



        self.tk.mainloop()





run = Set_up()

run.menu()
