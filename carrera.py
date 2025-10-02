class carrera:
    def __init__(self, nombre_carrera ,id_carrera=""):
        self.__id_carrera = id_carrera
        self.__nombre_carrera = nombre_carrera
#getter and setter
    def getter(self):
        return self.__nombre_carrera
   
    def setter(self, nuevo_nombre):
        self.__nombre_carrera = nuevo_nombre 
   
    def getter_id(self):
       return self.__id_carrera
    def __str__(self):
        return f"{self.__id_carrera} -> {self.__nombre_carrera}"
#end of file carrera.py