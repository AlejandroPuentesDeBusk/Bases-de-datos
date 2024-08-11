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


    def add_data(self, nom_tabla, columnas, valores):

        cur = self.obtener_cursor()

        consulta_sql = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values}) ").format(
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

        



        



def main():

    #Objeto
    ejecutar = Consultas("localhost", "postgres", "0711white", "postgres")

    #Ejecutamos
    ejecutar.connect_libreria()
    ejecutar.view_data("categorias")


    #Añadir datos a Autores

    #columnas_autores = ["nombre","apellido_paterno","nacionalidad","fecha_nacimiento"]
    #valores_autores = ["Gabriel","Garcia","Colombiana","1927-03-06"]

    #iniciar.add_data("autores",columnas_autores,valores_autores)


if __name__ == "__main__":
    main()

#cursor = connection.cursor()





