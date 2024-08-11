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

        try:
            cur.execute(consulta_sql)

            for result in cur.fetchall():

                print(result)
            
            cur.close()


        except psycopg2.Error as e:

            print("Querry unsuccesful")


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









        



        



def main():

    #Objeto
    ejecutar = Consultas("localhost", "postgres", "0711white", "postgres")

    #Ejecutamos
    ejecutar.connect_libreria()



    ###VER TODOS LOS DATOS DE UNA TABLA
    #ejecutar.view_data("categorias")


    #####Añadir datos a Autores

    #columnas_autores = ["nombre","apellido_paterno","nacionalidad","fecha_nacimiento"]
    #valores_autores = ["Gabriel","Garcia","Colombiana","1927-03-06"]
    #ejecutar.add_data("autores",columnas_autores,valores_autores)

    ######Anadir editorial
    #columnas_editoriales = ["nombre","telefono","correo_electronico"]
    #valores_editoriales = ["Sudamericana","5678230965","sudamericana@gmail.com"] 
    #ejecutar.add_data("editoriales",columnas_editoriales,valores_editoriales)


    #ELIMINAR UN REGISTRO DE UNA TABLA

    #ejecutar.del_data("editoriales","id_editorial",3)

    ###INNER JOIN entre USUARIOS Y PRESTAMOS

    ejecutar.inner_join()


if __name__ == "__main__":
    main()

#cursor = connection.cursor()





