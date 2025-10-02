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
def añadir_carrea(cur,nombre_carrera):
    try:
        cur.execute(f"insert into carrera (`Nombre_Carrera`) alues ('{nombre_carrera}')")
    except:
        print("Error al insertar la carrera")
def modificar_carrera(cur,nombre_carrera,id_carrera):
    try:
        cur.execute(f"update carrera set Nombre_Carrera='{nombre_carrera}' where id_Carrera={id_carrera}")
    except:
        print("Error al modificar la carrera")  
def ver_carreras(cur):
    try:
       return cur.execute(f"select * from carrera")
    except:
        print("Error al ver las carreras")
def borrar_carrera(cursor,id_carrera):
    try:
        cursor.execute(f"delete from carrera where id_Carrera={id_carrera}")
    except:
        print("Error al borrar la carrera")  

