# gestor_carreras.py

carreras = ['Mates', 'Català', 'Historia', 'Economia']

def mostrar_menu():
    print("\n--- MENÚ GESTOR DE CARRERAS ---")
    print("1. Añadir carrera")
    print("2. Actualizar carrera")
    print("3. Ver carreras")
    print("4. Borrar carrera")
    print("5. Salir")


def añadir_carrera():
    nombre = input("Introduce el nombre de la carrera: ")
    carreras.append(nombre)
    print(f"'Carrera' {nombre} ' añadida con éxito'")


def actualizar_carrera():
    print(f"{carreras}")
    carreraDelete = input("Que carrera desea Actualizar? : ")
    






# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        añadir_carrera()

    if opcion == "2":
        actualizar_carrera()
    else:
        print("Opción no válida.")