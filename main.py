import mysql.connector
import dao_Carrera as dao

# gestor_carreras.py

conexion = dao.connect_db()
cursor = conexion.cursor()

def mostrar_menu():
    print("\n--- MENÚ GESTOR DE CARRERAS ---")
    print("1. Añadir carrera")
    print("2. Actualizar carrera")
    print("3. Ver carreras")
    print("4. Borrar carrera")
    print("5. Salir")

def añadir_carrera(cursor):
    nombre = input("Introduce el nombre de la carrera: ")
    dao.añadir_carrea(cursor, nombre)
    conexion.commit()
    print(f"la carrera {nombre} se ha añadido.")
    ver_carreras(cursor)

def actualizar_carrera():
    ver_carreras()
    id_carrera = input("Introduce el ID de la carrera a actualizar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    sql = "UPDATE carreras SET nombre = %s WHERE id = %s"
    cursor.execute(sql, (nuevo_nombre, id_carrera))
    conexion.commit()
    print("Carrera actualizada.")

def ver_carreras(cursor):
    dao.ver_carreras(cursor)
    resultados = cursor.fetchall()
    if not resultados:
        print("No hay carreras registradas.")
    else:
        print("\n--- LISTA DE CARRERAS ---")
        for (Nombre_Carrera) in resultados:
            print(f"{Nombre_Carrera}")
        input("press any key to continue.....")

def borrar_carrera(cursor    ):
    id_carrera = input("Introduce el ID de la carrera a borrar: ")
    dao.borrar_carrera(cursor,id_carrera)
    conexion.commit()
    print("Carrera borrada.")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        añadir_carrera(cursor)
    elif opcion == "2":
        actualizar_carrera(cursor)
    elif opcion == "3":
        ver_carreras(cursor)
    elif opcion == "4":
        borrar_carrera(cursor)
    elif opcion == "5":
        cursor.close()
        conexion.close()
    else:
        print("Opción no válida.")