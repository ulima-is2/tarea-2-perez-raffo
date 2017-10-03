import sqlite3
conn = sqlite3.connect(':memory:')

# Clase conectar BD
class Conectar():

    # Funcion crear tablas
    def CrearTablas(self):
        c = conn.cursor()
        #Crear tabla de cines
        c.execute('''CREATE TABLE CINE
                         (id_cine int PRIMARY KEY, nombreCine text )''')

        # Crear tabla de peliculas
        c.execute('''CREATE TABLE PELICULA
                         (id_pelicula int PRIMARY KEY, nombrePeli text )''')
       
        # Crear tabla de cines con referencia a película
        c.execute('''CREATE TABLE PELI_CINE
                        (id_cine int, id_pelicula int,
                        PRIMARY KEY (id_cine, id_pelicula),
                        FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula)
                        )''') 

        # Crear tabla de funciones
        c.execute('''CREATE TABLE FUNCION
                        (id_funcion int PRIMARY KEY, id_cine int, id_pelicula, hora int, min int,
                        FOREIGN KEY(id_cine, id_pelicula) REFERENCES PELI_CINE(id_cine, id_pelicula)
                            )''')

        # Crear tabla de entradas
        c.execute('''CREATE TABLE ENTRADA
                        (id_entrada INTEGER PRIMARY KEY AUTOINCREMENT, id_funcion int, cantidad int,
                        FOREIGN KEY(id_funcion) REFERENCES FUNCION(id_funcion)
                        )''')

        # cerrar conexion
        conn.commit()
        c.close()

    # funcion insertar elementos
<<<<<<< HEAD
    def inserts(self):
=======
    def InsertarE(self):
>>>>>>> 0eeae41f4e4a8d18ec59b9cf5fdf34a49ac64ae0

        c = conn.cursor()

        # ingresar cines
        c.execute("INSERT into CINE values (1,'CinePlaneta')")

        c.execute("INSERT into CINE values (2,'CineStark')")

        # ingresar películas
        c.execute("INSERT into PELICULA values (1,'IT')")
        c.execute("INSERT into PELICULA values (2,'La hora Final')")
        c.execute("INSERT into PELICULA values (3,'Desaparecido')")
        c.execute("INSERT into PELICULA values (4,'Deep el Pulpo')")


        #ingresar peliculas por cine cinePlaneta

        c.execute("INSERT into PELI_CINE values (1,1)")

        c.execute("INSERT into PELI_CINE values (1,2)")

        c.execute("INSERT into PELI_CINE values (1,3)")
        c.execute("INSERT into PELI_CINE values (1,4)")

        #ingresar peliculas por cine cinestark

        c.execute("INSERT into PELI_CINE values (2,3)")
        c.execute("INSERT into PELI_CINE values (2,4)")

        #ingresar funciones de cine Cineplaneta

        c.execute("INSERT into FUNCION values (1,1,1,19,0)")

        c.execute("INSERT into FUNCION values (2,1,1,20,30)")

        c.execute("INSERT into FUNCION values (3,1,1,22,0)")

        c.execute("INSERT into FUNCION values (4,1,2,21,0)")

        c.execute("INSERT into FUNCION values (5,1,3,20,0)")

        c.execute("INSERT into FUNCION values (6,1,3,23,0)")

        c.execute("INSERT into FUNCION values (7,1,4,16,0)")


        #ingresar funciones de cine cineStark

        c.execute("INSERT into FUNCION values (8,2,3,21,0)")

        c.execute("INSERT into FUNCION values (9,2,3,23,0)")

        c.execute("INSERT into FUNCION values (10,2,4,16,0)")

        c.execute("INSERT into FUNCION values (11,2,4,20,0)")   


        c.close()

    # Funcion listar cines 
<<<<<<< HEAD
    def listar_Cines(self):
=======
    def listarCines(self):
>>>>>>> 0eeae41f4e4a8d18ec59b9cf5fdf34a49ac64ae0
        c = conn.cursor()
        c.execute("SELECT * FROM CINE")
        R = c.fetchall()
        pass

    # funcion listar peliculas
<<<<<<< HEAD
    def listar_peliculas(self, id_cine):
=======
    def listarPeliculas(self, id_cine):
>>>>>>> 0eeae41f4e4a8d18ec59b9cf5fdf34a49ac64ae0
        c = conn.cursor()
        c.execute("""SELECT PELICULA.id_pelicula, nombrePeli FROM PELICULA
            JOIN PELI_CINE ON PELICULA.id_pelicula = PELI_CINE.id_pelicula 
            WHERE id_cine = (?)""", (id_cine,) )
        R = c.fetchall()
        x = []
        for r in R:
            x.append(Pelicula(r[0],r[1]))
        c.close() 
        return x
        
    # funcion listar funciones
<<<<<<< HEAD
    def listar_funciones(self, id_cine, id_pelicula):
=======
    def listarFunciones(self, id_cine, id_pelicula):
>>>>>>> 0eeae41f4e4a8d18ec59b9cf5fdf34a49ac64ae0
        c = conn.cursor()
        c.execute("""SELECT id_funcion, id_cine, id_pelicula, hora, min FROM FUNCION 
            WHERE id_cine = (?) and id_pelicula = (?)""", (id_cine, id_pelicula) )
        R = c.fetchall()
        x = []
        for r in R:
            x.append(Funcion(r[0],r[3],r[4]))
        c.close() 
        return x

     #Funcion añadir entrada
<<<<<<< HEAD
    def anadir_entrada(self, id_pelicula, id_funcion, cantidad):
=======
    def anadirEntrada(self, id_pelicula, id_funcion, cantidad):
>>>>>>> 0eeae41f4e4a8d18ec59b9cf5fdf34a49ac64ae0
        c = conn.cursor()
        c.execute("""INSERT INTO ENTRADA(id_funcion, cantidad)
            VALUES (?, ?)""", (id_funcion, cantidad) )
        x = Entrada(c.lastrowid, id_pelicula, id_funcion, cantidad)
        c.close()
        return x

    # funcion listar entradas
<<<<<<< HEAD
    def listar_entradas(self, id_funcion):
=======
    def listarEntradas(self, id_funcion):
>>>>>>> 0eeae41f4e4a8d18ec59b9cf5fdf34a49ac64ae0
        c = conn.cursor()
        c.execute("""SELECT E.id_entrada, F.id_pelicula, E.id_funcion, E.cantidad FROM ENTRADA E
            JOIN FUNCION F ON E.id_funcion = F.id_funcion
            WHERE id_funcion = ? """, (id_funcion) )
        R = c.fetchall()
        x = []
        for r in R:
            x.append(Entrada(r[0], r[1], r[2], r[3]))
        c.close() 
        return x

   
    