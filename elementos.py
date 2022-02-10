import os

class Poste:

    contador = 0

    def __init__(self, num_apoyos, num_elemento) -> None:

        self.id = num_elemento
        file = open(f"estado_poste_{self.id}.txt", "w")

        if (num_apoyos == 5):
            self.nombre = "poste normal"
            file.write(f"Se ha creado el elemento: <{self.nombre} {num_elemento}>" + os.linesep)
            
        else:
            self.nombre = "poste grande"
            file.write(f"Se ha creado un elemento: <{self.nombre} {num_elemento}>" + os.linesep)

        file.close()

    def conexion(self, elemento):
        print("a")

    def instalacion(self):
        print("a")

    def reporte(self):
        file = open(f"estado_poste_{self.id}.txt", "r")
        print(file.read())
        file.close()


class Transformador:

    def __init__(self, num_elemento) -> None:
        self.nombre = f"transformador {num_elemento}"


class Relay:

    def __init__(self, num_elemento) -> None:
        self.nombre = f"relay {num_elemento}"


class Linea:

    def __init__(self, tipo=0) -> None:
        
        if (tipo == 1):
            self.nombre = "linea alta tension"
        else:
            self.nombre = "linea media tension"

