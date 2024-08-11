import psycopg2

#Datos de conexion



class Consultas:

    def __init__(self, host, user, password, data_base):


        self.host = host
        self.user = user
        self.password = password
        self.data_base = data_base



    def connect_libreria(self):

        try:
            connection = psycopg2.connect(
                host = "localhost",
                user = "postgres",
                password = "0711white",
                database = "postgres",
            )

            print("Succesfully conected")

        except psycopg2.Error as e:

            print("Error, connection failed")



def main():

    #Objeto
    iniciar = Consultas("localhost", "postgres", "0711white", "postgres")

    #Ejecutamos
    iniciar.connect_libreria()


if __name__ == "__main__":
    main()

#cursor = connection.cursor()





