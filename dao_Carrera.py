import mysql.connector

def connect_db():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        #password="Bootcamp123"
        password="12345678",
        database="carreras")
    return cnx

# Get a cursor
def user_query(cur,query):
    try:
        cur.execute(query)
        return cur.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
####.execute("INSERT INTO table VALUES(%s,%s)", (int(id), string))

def añadir_carrera(cur,nombre_carrera,nota_corte,duracion):
    try:
        cur.execute("INSERT INTO carrera (Nombre_Carrera,Nota_de_corte,Duracion) VALUES (%s,%s,%s)", (nombre_carrera,nota_corte,duracion,))
    except mysql.connector.Error as err:
        print("Error al insertar la carrera:", err)
        
        
def modificar_carrera(cursor,nombre_carrera,id_carrera):
    try:
        cursor.execute("SELECT Nombre_Carrera FROM carrera where id_Carrera = %s", (id_carrera,))
        resultados = cursor.fetchall()
        cursor.execute("UPDATE carrera SET Nombre_Carrera= %s WHERE id_Carrera = %s", (nombre_carrera,id_carrera,))
        return resultados
    except mysql.connector.Error as err:
        print("Error al modificar la carrera :", err) 
         
def ver_carreras(cur):
    try:
        cur.execute("SELECT * FROM carrera")
        return cur.fetchall()
    except mysql.connector.Error as err:
        print("Error al ver las carreras :", err)
        
def borrar_carrera(cursor,id_carrera):
    try:         
        cursor.execute("SELECT Nombre_Carrera FROM carrera WHERE id_Carrera = %s", (id_carrera,))
        resultados = cursor.fetchall()
        cursor.execute("DELETE from carrera WHERE id_Carrera = %s", (id_carrera,))
        return resultados
    except mysql.connector.Error as err:
        print("Error al borrar la carrera: ",err)  

