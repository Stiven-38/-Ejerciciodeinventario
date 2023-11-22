
# Diccionario para almacenar la informacion de los equipos
equipos = {}

# Funcion para agregar un equipo al diccionario
def agregarEquipo(idEquipo, cargador, mouse, ambiente):
    equipos[idEquipo] = {'ID': idEquipo, 'Cargador': cargador, 'Mouse': mouse, 'Ambiente': ambiente, 'Novedades': []}

# Funcion para agregar una novedad a un equipo
def agregarNovedad(idEquipo, fecha, descripcion):
    if idEquipo in equipos:
        equipos[idEquipo]['Novedades'].append({'Fecha': fecha, 'Descripcion': descripcion})
        print("La novedad ha sido agregada con exito al equipo con ID {}.".format(idEquipo))
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Funcion para generar un reporte de equipos con novedades
def reporteNovedades():
    equiposConNovedades = [equipo for equipo in equipos.values() if equipo['Novedades']]
    return equiposConNovedades

# Funcion para mostrar la informacion de todos los equipos
def mostrarEquipos():
    for equipo in equipos.values():
        print("ID: {}".format(equipo['ID']))
        print("Cargador: {}".format(equipo['Cargador']))
        print("Mouse: {}".format(equipo['Mouse']))
        print("Ambiente: {}".format(equipo['Ambiente']))
        print("Novedades:")
        for novedad in equipo['Novedades']:
            print("- Fecha: {}, Descripcion: {}".format(novedad['Fecha'], novedad['Descripcion']))
        print("-------------")

# Funcion para modificar la informacion de un equipo
def modificarEquipo(idEquipo, cargador, mouse, ambiente):
    if idEquipo in equipos:
        equipos[idEquipo]['Cargador'] = cargador
        equipos[idEquipo]['Mouse'] = mouse
        equipos[idEquipo]['Ambiente'] = ambiente
    else:
        print("El equipo con ID {} no existe.".format(idEquipo)) 

# Funcion para eliminar un equipo del diccionario
def eliminarEquipo(idEquipo):
    if idEquipo in equipos:
        del equipos[idEquipo]
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

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
                print("Datos del equipo:")
                print("ID: {}".format(equipos[idEquipo]['ID']))
                print("Cargador: {}".format(equipos[idEquipo]['Cargador']))
                print("Mouse: {}".format(equipos[idEquipo]['Mouse']))
                print("Ambiente: {}".format(equipos[idEquipo]['Ambiente']))
            else:
                print("El equipo no se encuentra en la base de datos")
        elif opcion.lower() == '4':
            # Mostrar un reporte de equipos con novedades
            equiposNovedades = reporteNovedades()
            if not equiposNovedades:
                print("No hay ninguna novedad en los equipos")
            else:
                for equipo in equiposNovedades:
                    print("ID: {}".format(equipo['ID']))
                    for novedad in equipo['Novedades']:
                        print("- Fecha: {}, Descripcion: {}".format(novedad['Fecha'], novedad['Descripcion']))
        elif opcion.lower() == '5':
            # Mostrar la informacion de todos los equipos
            mostrarEquipos()
        elif opcion.lower() == '6':
            # Modificar informacion de un equipo
            idEquipo = input("Ingrese el ID del equipo que desea modificar: ")
            cargador = input("El equipo cuenta con cargador? (si/no): ")
            mouse = input("El equipo cuenta con mouse? (si/no): ")
            ambiente = input("En qué ambiente se encuentra el equipo?: ")
            modificarEquipo(idEquipo, cargador, mouse, ambiente)
        elif opcion.lower() == '7':
            # Eliminar un equipo
            idEquipo = input("Ingrese el ID del equipo que desea eliminar: ")
            eliminarEquipo(idEquipo)
        elif opcion.lower() == '8':
            # Salir del programa
            break
        else:
            # Opcion no valida
            print("La opción que ingresó no es válida, verifique las opciones e ingrese una correcta")
    
    # Mensaje de finalizacion
    print("El programa ha terminado con éxito :")

# Llamada a la funcion principal para iniciar el programa
menu()
