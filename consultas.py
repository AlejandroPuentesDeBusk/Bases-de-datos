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

        cur = self.con.cursor()



    #Asi podemos usar cur dentro de toda la clase
    def obtener_cursor(self):
        
        if not self.con:
            print("NO hay conexion")

        return self.con.cursor()
    



    def view_data(self,n_tabla):

        cur = self.obtener_cursor()

        consulta_sql = sql.SQL("SELECT * FROM {table};"). format(
            table= sql.Identifier(n_tabla)
        )

        try:
            cur.execute(consulta_sql)

            for result in cur.fetchall():

                print(result)
            
            cur.close()


        except psycopg2.Error as e:

            print("Querry unsuccesful")



        







def main():

    #Objeto
    iniciar = Consultas("localhost", "postgres", "0711white", "postgres")

    #Ejecutamos
    iniciar.connect_libreria()
    iniciar.view_data("categorias")


if __name__ == "__main__":
    main()

#cursor = connection.cursor()





