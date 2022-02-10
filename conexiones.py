import elementos as e

#creacion de postes
poste_1 = e.Poste(1, 5)
poste_2 = e.Poste(2, 8)
poste_3 = e.Poste(3, 5)

#creacion de elementos
transfromador_1 = e.Transformador(1)
relay_1 = e.Relay(1)
relay_2 = e.Relay(2)
relay_3 = e.Relay(3)

#creacion de lineas
alta_tension = e.Linea(1)
media_tension = e.Linea()

#instalacion de elementos
poste_3.instalacion(transfromador_1)
poste_1.instalacion(relay_1)
poste_2.instalacion(relay_2)
poste_3.instalacion(relay_3)

#conexion de postes
poste_2.conexion(poste_1, media_tension)
poste_2.conexion(poste_3, media_tension)
poste_1.conexion(poste_3, alta_tension)
poste_1.conexion(poste_3, media_tension)
poste_3.conexion(poste_2, alta_tension)

#impresion del estado de cada poste
poste_1.reporte()
poste_2.reporte()
poste_3.reporte()
