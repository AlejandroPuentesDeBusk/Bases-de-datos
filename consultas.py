import psycopg2
from psycopg2 import sql

#Datos de conexion



class Consultas:

    def __init__(self, host, user, password, data_base):


        self.host = host
        self.user = user
        self.password = password
        self.data_base = data_base
        self.con = None


    def connect_libreria(self):

        try:
            self.con = psycopg2.connect(
                host = "localhost",
                user = "postgres",
                password = "0711white",
                database = "postgres",
            )

            print("Succesfully conected")

        except psycopg2.Error as e:

            print("Error, connection failed")


    #Asi podemos usar cur dentro de toda la clase
    def obtener_cursor(self):
        
        if not self.con:
            print("NO hay conexion")

        return self.con.cursor()
    


#Ver toda la info de una tabla
    def view_data(self,nom_tabla):

        cur = self.obtener_cursor()

        consulta_sql = sql.SQL("SELECT * FROM {table};"). format(
            table= sql.Identifier(nom_tabla)
        )

        #La ejecutamos

        data_list= []

        try:
            cur.execute(consulta_sql)

            for titulo in cur.description:
                data_list.append(titulo[0])

            for result in cur.fetchall():

                data_list.append(result)

            cur.close()
            return data_list
            


        except psycopg2.Error as e:

            print("Querry unsuccesful")
            cur.close()


#Añadir una querry a cualquier tabla
    def add_data(self, nom_tabla, columnas, valores):

        cur = self.obtener_cursor()

        consulta_sql = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values});").format(
            table = sql.Identifier(nom_tabla),
            fields = sql.SQL(', ').join(map(sql.Identifier, columnas)),
            values = sql.SQL(', ').join(sql.Placeholder() for i in valores))
        
        try: 

            cur.execute(consulta_sql, valores)
            self.con.commit()
            print("Change succesfull and commited")
            cur.close()

        except psycopg2.Error as e:

            print("Querry unsuccesful")
            self.con.rollback()
            cur.close()


#Eliminar un registro NUEVO sin relacion a otras tablas o ELIMINAR USUARIO Y SUS PRETAMOS

    def del_data(self,nom_tabla,columna, id_thing):

        cur = self.obtener_cursor()

        consulta_sql = sql.SQL("DELETE FROM {table} WHERE {data_colum} = %s ;"). format(
            table = sql.Identifier(nom_tabla),
            data_colum = sql.Identifier(columna),

        )

        #Nota el id_thing es una TUPLA 

        try:
            cur.execute(consulta_sql, (id_thing,))
            self.con.commit()
            print(f"{id_thing} from table {nom_tabla}, was deleted succesfuly")
            cur.close()

        except psycopg2.Error as e:

            print("Querry unsuccesful")
            self.con.rollback()
            cur.close()


#Objetemos los prestamos de cada usuario 
    def inner_join(self):

        cur = self.obtener_cursor()

        consulta_sql = ("SELECT usuarios.nombre, prestamos.* FROM usuarios INNER JOIN prestamos ON usuarios.id_usuario = prestamos.id_usuario;" )

        try:

            cur.execute(consulta_sql)

            column_title= []

            for titulo in cur.description:
                column_title.append(titulo[0])

            print(column_title)

            for result in cur.fetchall():

                print(result)

            cur.close()
            print("Querry result succesfull")

        except psycopg2.Error as e:

            print("Querry unsuccesful")
            cur.close()


####JOIN GLOBAL PRUEBA FUE UN EXITO

    def inner_join_g(self, p_pequeña, nom_tabla_1, nom_tabla_2, con_1):

        cur = self.obtener_cursor()

        ##usuarios.nombre

        consulta_sql = sql.SQL("SELECT {tabla_1}.{pequeña}, {tabla_2}.* FROM {tabla_1} INNER JOIN {tabla_2} ON {tabla_1}.{id} = {tabla_2}.{id};" ).format(
            pequeña= sql.Identifier(p_pequeña),
            tabla_1 = sql.Identifier(nom_tabla_1),
            tabla_2 = sql.Identifier(nom_tabla_2),
            id = sql.Identifier(con_1),
        
        )


        try:

            cur.execute(consulta_sql)

            column_title= []

            for titulo in cur.description:
                column_title.append(titulo[0])

            print(column_title)

            for result in cur.fetchall():

                print(result)

            cur.close()
            print("Querry result succesfull")

        except psycopg2.Error as e:

            print("Querry unsuccesful")
            cur.close()







        



        



def main():

    #Objeto
    ejecutar = Consultas("localhost", "postgres", "0711white", "postgres")

    #Ejecutamos
    ejecutar.connect_libreria()


#___________________________________________________________________________________________________
    ###VER TODOS LOS DATOS DE UNA TABLA
    #ejecutar.view_data("categorias")
    ejecutar.view_data("libros")

#_____________________________________________________________________________________________________
    #####Añadir datos a Autores
    #columnas_autores = ["nombre","apellido_paterno","nacionalidad","fecha_nacimiento"]
    #valores_autores = ["Gabriel","Garcia","Colombiana","1927-03-06"]
    #ejecutar.add_data("autores",columnas_autores,valores_autores)

    columnas_libros=["titulo","id_autor","id_editorial","año_publicacion","id_categoria","id_librero"]
    valores_libros = ['El Amor en Tiempos De Colera', 3, 2, '1990-01-01', 2, 1]
    ejecutar.add_data("libros",columnas_libros,valores_libros)

    ######Anadir editorial
    #columnas_editoriales = ["nombre","telefono","correo_electronico"]
    #valores_editoriales = ["Sudamericana","5678230965","sudamericana@gmail.com"] 
    #ejecutar.add_data("editoriales",columnas_editoriales,valores_editoriales)
#__________________________________________________________________________________________________
    #ELIMINAR UN REGISTRO DE UNA TABLA

    ######### ELiminar editorial
    #ejecutar.del_data("editoriales","id_editorial",3)

#__________________________________________________________________________________________________
    ####Uso inner_join_g  

    #1. columna tabla 1
    #2. nombre tabla 1
    #3 nombre tabla 2
    #4 dato en comun


    #Para usuarios y prestamo
    #ejecutar.inner_join_g("nombre","usuarios","prestamos","id_usuario")

    #para autor y libros
    #ejecutar.inner_join_g("nombre","autores","libros","id_autor")


if __name__ == "__main__":
    main()

#cursor = connection.cursor()





