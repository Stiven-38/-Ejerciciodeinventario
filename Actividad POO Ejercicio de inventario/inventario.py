class Equipo:
    def __init__(self, idEquipo, cargador, mouse, ambiente):
        self.ID = idEquipo
        self.Cargador = cargador
        self.Mouse = mouse
        self.Ambiente = ambiente
        self.Novedades = []

    def agregarNovedad(self, fecha, descripcion):
        self.Novedades.append({'Fecha': fecha, 'Descripcion': descripcion})
        print(f"La novedad ha sido agregada con éxito al equipo con ID {self.ID}.")

    def mostrarInformacion(self):
        print(f"ID: {self.ID}")
        print(f"Cargador: {self.Cargador}")
        print(f"Mouse: {self.Mouse}")
        print(f"Ambiente: {self.Ambiente}")
        print("Novedades:")
        for novedad in self.Novedades:
            print(f"- Fecha: {novedad['Fecha']}, Descripcion: {novedad['Descripcion']}")
        print("-------------")

# Diccionario para almacenar la informacion de los equipos
equipos = {}

# Funcion para agregar un equipo al diccionario
def agregarEquipo(idEquipo, cargador, mouse, ambiente):
    equipos[idEquipo] = Equipo(idEquipo, cargador, mouse, ambiente)

# Funcion para agregar una novedad a un equipo
def agregarNovedad(idEquipo, fecha, descripcion):
    if idEquipo in equipos:
        equipos[idEquipo].agregarNovedad(fecha, descripcion)
    else:
        print(f"El equipo con ID {idEquipo} no existe.")

# Funcion principal que presenta un menu interactivo al usuario
def menu():
    while True:
        # Mostrar las opciones del menu
        print("Opciones de la aplicación:")
        print("1. Agregar un equipo de cómputo")
        print("2. Agregar una novedad sobre un equipo")
        print("3. Buscar un equipo por ID")
        print("4. Mostrar reporte de equipos con novedades")
        print("5. Mostrar todos los equipos")
        print("6. Modificar información de un equipo")
        print("7. Eliminar un registro de cómputo")
        print("8. Salir")

        # Solicitar al usuario que elija una opcion
        opcion = input("Digite la opción que desea realizar: ")

        # Manejar las diferentes opciones
        if opcion.lower() == '1':
            # Agregar un nuevo equipo
            idEquipo = input("Ingrese el ID del equipo que desea agregar: ")
            cargador = input("El equipo cuenta con cargador? (si/no): ")
            mouse = input("El equipo cuenta con mouse? (si/no): ")
            ambiente = input("En qué ambiente se encuentra el equipo?: ")
            agregarEquipo(idEquipo, cargador, mouse, ambiente)
        elif opcion.lower() == '2':
            # Agregar una novedad a un equipo existente
            idEquipo = input("Ingrese el ID del equipo al que le va a registrar una novedad: ")
            fecha = input("Ingrese la fecha de la novedad: ")
            descripcion = input("Ingrese la descripción de la novedad: ")
            agregarNovedad(idEquipo, fecha, descripcion)
        elif opcion.lower() == '3':
            # Buscar un equipo por ID y mostrar su informacion
            idEquipo = input("Ingrese el ID del equipo que desea buscar: ")
            if idEquipo in equipos:
                equipos[idEquipo].mostrarInformacion()
            else:
                print("El equipo no se encuentra en la base de datos")
        elif opcion.lower() == '4':
            # Mostrar un reporte de equipos con novedades
            equiposNovedades = [equipo for equipo in equipos.values() if equipo.Novedades]
            if not equiposNovedades:
                print("No hay ninguna novedad en los equipos")
            else:
                for equipo in equiposNovedades:
                    equipo.mostrarInformacion()
        elif opcion.lower() == '5':
            # Mostrar la informacion de todos los equipos
            for equipo in equipos.values():
                equipo.mostrarInformacion()
        elif opcion.lower() == '6':
            # Modificar informacion de un equipo
            idEquipo = input("Ingrese el ID del equipo que desea modificar: ")
            cargador = input("El equipo cuenta con cargador? (si/no): ")
            mouse = input("El equipo cuenta con mouse? (si/no): ")
            ambiente = input("En qué ambiente se encuentra el equipo?: ")
            if idEquipo in equipos:
                equipos[idEquipo].Cargador = cargador
                equipos[idEquipo].Mouse = mouse
                equipos[idEquipo].Ambiente = ambiente
            else:
                print(f"El equipo con ID {idEquipo} no existe.")
        elif opcion.lower() == '7':
            # Eliminar un equipo
            idEquipo = input("Ingrese el ID del equipo que desea eliminar: ")
            if idEquipo in equipos:
                del equipos[idEquipo]
            else:
                print(f"El equipo con ID {idEquipo} no existe.")
        elif opcion.lower() == '8':
            # Salir del programa
            break
