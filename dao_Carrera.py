import mysql.connector
cnx = None
def connect_db(cnx):
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        #password="Bootcamp123"
        password="12345678",
        database="carreras")
    return cnx

# Get a cursor
cur = cnx.cursor()
def añadir_carrea(nombre_carrera):
    try:
        cur.execute("insert into carrera (Nombre_Carrera) values ('nombre_carrera')")
    except:
        print("Error al insertar la carrera")
def modificar_carrera(nombre_carrera,id_carrera):
    try:
        cur.execute("update carrera set Nombre_Carrera='{nombre_carrera}', where id_Carrera={id_carrera}")
    except:
        print("Error al modificar la carrera")  
def ver_carreras():
    try:
        cur.execute("select * from carrera")
    except:
        print("Error al ver las carreras")
def borrar_carrera(id_carrera):
    try:
        cur.execute("delete from carrera where id_Carrera={id_carrera}")
    except:
        print("Error al borrar la carrera")  

cur.close()
cnx.close()