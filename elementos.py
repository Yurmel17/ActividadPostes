import os

class Poste:

    conexiones = 0
    instalaciones = 0

    def __init__(self, num_elemento, num_apoyos) -> None:
        self.num_elemento = num_elemento
        file = open(f"estado_poste_{self.num_elemento}.txt", "w")

        if (num_apoyos == 5):
            self.nombre = "poste normal"
            self.apoyos = 5
            file.write(f"Se ha creado el elemento: <{self.nombre} {self.num_elemento}>" + os.linesep)
        else:
            self.nombre = "poste grande"
            self.apoyos = 8
            file.write(f"Se ha creado un elemento: <{self.nombre} {self.num_elemento}>" + os.linesep)

        file.close()


    def conexion(self, elemento, linea):
        file1 = open(f"estado_poste_{self.num_elemento}.txt", "a+")
        file2 = open(f"estado_poste_{elemento.num_elemento}.txt", "a+")
        
        self.conexiones += 1
        elemento.conexiones += 1

        if (self.conexiones + self.instalaciones) < 6:
            file1.write(f"Se ha creado una conexión entre el <{self.nombre} {self.num_elemento}> y el <{elemento.nombre} {elemento.num_elemento}> a traves de una {linea.nombre}" + os.linesep)
            file2.write(f"Se ha creado una conexión entre el <{self.nombre} {self.num_elemento}> y el <{elemento.nombre} {elemento.num_elemento}> a traves de una {linea.nombre}" + os.linesep)        
        else:
            file1.write(f"El elemento <{self.nombre} {self.num_elemento}> se ha quedado sin apoyos y no acepta mas conexiones" + os.linesep)
            self.conexiones -= 1
            elemento.conexiones -= 1
        
        file1.close()
        file2.close()

    def instalacion(self, elemento):
        file = open(f"estado_poste_{self.num_elemento}.txt", "a+")
        self.instalaciones += 1
       
        if (self.conexiones + self.instalaciones) < 6:
            file.write(f"Se ha instalado un <{elemento.nombre}> en el <{self.nombre} {self.num_elemento}>" + os.linesep)
        else:
            file.write(f"El elemento <{self.nombre} {self.num_elemento}> se ha quedado sin apoyos y no acepta mas conexiones" + os.linesep)
       
        file.close()

    def reporte(self):
        file = open(f"estado_poste_{self.num_elemento}.txt", "a+")
        file.write(f"El elemento: <{self.nombre} {self.num_elemento}> tiene {self.apoyos - (self.conexiones + self.instalaciones)} apoyos libres")
      
        print(file.read())
        
        file.close()


class Transformador:

    def __init__(self, num_elemento) -> None:
        self.nombre = f"transformador {num_elemento}"
        self.num_elemento = num_elemento


class Relay:

    def __init__(self, num_elemento) -> None:
        self.nombre = f"relay {num_elemento}"
        self.num_elemento = num_elemento


class Linea:

    def __init__(self, tipo=0) -> None:
        
        if (tipo == 1):
            self.nombre = "linea de alta tension"
            self.tipo = 1
        else:
            self.nombre = "linea de media tension"
            self.tipo = 0
