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
        return None    
####.execute("INSERT INTO table VALUES(%s,%s)", (int(id), string))

def añadir_carrea(cur,nombre_carrera):
    try:
        cur.execute("insert into carrera (`Nombre_Carrera`) values (%s)", (nombre_carrera,))
    except:
        print("Error al insertar la carrera")
        
def modificar_carrera(cursor,nombre_carrera,id_carrera):
    try:
        cursor.execute("select Nombre_Carrera from carrera where id_Carrera = %s", (id_carrera,))
        resultados = cursor.fetchall()
        cursor.execute("update carrera set Nombre_Carrera= %s where id_Carrera = %s", (nombre_carrera,id_carrera,))
        return resultados
    except:
        print("Error al modificar la carrera") 
         
def ver_carreras(cur):
    try:
        cur.execute("select * from carrera")
        return cur.fetchall()
        
    except:
        print("Error al ver las carreras")
        
def borrar_carrera(cursor,id_carrera):
    try:         
        cursor.execute("select Nombre_Carrera from carrera where id_Carrera = %s", (id_carrera,))
        resultados = cursor.fetchall()
        cursor.execute("delete from carrera where id_Carrera = %s", (id_carrera,))
        return resultados
    except:
        print("Error al borrar la carrera")  

