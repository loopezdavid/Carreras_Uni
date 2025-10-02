import dao_Carrera as dao
import os
start_program = True
# Código para activar la negrita
NEGRITA = '\033[1m'
# Código para restablecer el formato (desactiva la negrita)
RESET = '\033[0m'
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
    print(f"\nla carrera {NEGRITA}{nombre}{RESET} se ha añadido.\n")
    input("press any key to continue.....")


def actualizar_carrera(cursor):
    id_carrera = input("Introduce el ID de la carrera a actualizar: ")
    nombre_carrera = input("Introduce el nuevo nombre de la carrera: ")
    resutlrados = dao.modificar_carrera(cursor,nombre_carrera,id_carrera)
    conexion.commit()
    for i in resutlrados:
        print(f"\nLa carrera {NEGRITA}{i[0]}{RESET} se ha modificado a {NEGRITA}{nombre_carrera}{RESET}.\n")
    input("press any key to continue.....")

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

def borrar_carrera(cursor):
    id_carrera = input("Introduce el ID de la carrera a borrar: ")
    resultados = dao.borrar_carrera(cursor,id_carrera)
    conexion.commit()
    if not resultados:
        print("\nCarrera no encontrada.\n")
    else:
        for i in resultados:
            print(f"\nLa carrera {NEGRITA}{i[0]}{RESET} se ha borrado.\n")
    input("press any key to continue.....")
#query personalizada 
def user_query(cursor):
    query = input("Introduce la consulta SQL: ")
    resultados=dao.user_query(cursor,query)
    if not resultados:
        print("No hay resultados.")
    else:
        for row in resultados:
            print(row)
    input("press any key to continue.....")
# Programa principal
while start_program:
    os.system('cls' if os.name == 'nt' else 'clear')
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
        print("\nSaliendo del programa...\n")
        start_program = False
    elif opcion == "0":
        user_query(cursor)
    else:
        print("Opción no válida.")