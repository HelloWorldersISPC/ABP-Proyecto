escenarios = []

escenarios_predefinidos = [
    {
        "nombre": "Apagar todo (apagar todos los dispositivos)",
        "acciones": lambda dispositivos: apagar_todo(dispositivos)
    },
    {
        "nombre": "Salida (apagar luces y encender cámaras)",
        "acciones": lambda dispositivos: salida(dispositivos)
    }
]

def apagar_todo(dispositivos):
    for disp in dispositivos:
        disp["estado"] = False

def salida(dispositivos):
    for disp in dispositivos:
        if disp["tipo"].lower() == "cámara":
            disp["estado"] = True
        elif disp["tipo"].lower() == "luz":
            disp["estado"] = False

def listar_escenarios():
    if not escenarios:
        print("No hay escenarios disponibles.")
        return
    print("\nEscenarios disponibles:")
    for i, esc in enumerate(escenarios, 1):
        print(f"{i}. {esc['nombre']}")

def usar_escenario(escenarios, dispositivos):
    if not escenarios:
        print("No hay escenarios disponibles.")
        return

    print("\nEscenarios disponibles:")
    for i, escenario in enumerate(escenarios, 1):
        print(f"{i}. {escenario['nombre']}")
    print("0. Volver al menú principal")

    opcion_input = input("Seleccione el número del escenario a aplicar: ")
    if not opcion_input.isdigit():
        print("Entrada inválida. Debe ingresar un número.")
        return

    opcion = int(opcion_input)

    if opcion == 0:
        return
    if opcion < 1 or opcion > len(escenarios):
        print("Opción inválida.")
        return

    escenario = escenarios[opcion - 1]

    if callable(escenario['acciones']):
        escenario['acciones'](dispositivos)
    else:
        for accion in escenario['acciones']:
            for dispositivo in dispositivos:
                if dispositivo['nombre'] == accion['nombre']:
                    dispositivo['estado'] = accion['estado']

    print(f"Escenario '{escenario['nombre']}' aplicado.")


def agregar_escenario(escenarios):
    tipos_disponibles = ["Luz", "Cámara", "Aire acondicionado", "Lavarropa"]

    while True:
        print("\n1. Crear escenario")
        print("0. Volver al menú principal")
        opcion_inicio = input("Seleccione una opción: ").strip()

        if opcion_inicio == "0":
            return
        elif opcion_inicio != "1":
            print("Opción inválida.")
            continue

        nombre = input("Ingrese el nombre del nuevo escenario: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue

        print("Definirá acciones para el escenario:")

        acciones_por_tipo = {}
        configuracion_aires = {}
        tipos_seleccionados = set()

        while True:
            print("\nTipos de dispositivos disponibles:")

            disponibles_no_seleccionados = [tipo for tipo in tipos_disponibles if tipo.lower() not in tipos_seleccionados]

            for i, tipo in enumerate(disponibles_no_seleccionados, 1):
                print(f"{i}. {tipo}")

            if acciones_por_tipo:
                print("0. Finalizar escenario")
            else:
                print("0. Volver al menú principal")

            opcion = input("Seleccione el número del tipo de dispositivo para definir acción: ").strip()

            if opcion == '0':
                if acciones_por_tipo:
                    def acciones_func(dispositivos):
                        for disp in dispositivos:
                            tipo_disp = disp["tipo"].lower()
                            accion = acciones_por_tipo.get(tipo_disp, 's')
                            if accion == 'e':
                                disp["estado"] = True
                                if tipo_disp == "aire acondicionado":
                                    disp["modo"] = configuracion_aires.get("modo", "Frío")
                                    disp["temperatura"] = configuracion_aires.get("temperatura", 24)
                            elif accion == 'a':
                                disp["estado"] = False

                    escenario = {
                        "nombre": nombre,
                        "acciones": acciones_func
                    }
                    escenarios.append(escenario)
                    print(f"\nEscenario '{nombre}' creado correctamente.\n")
                else:
                    print("\nNo se definieron acciones. Volviendo al menú principal.\n")
                return  # Siempre vuelve al menú principal

            if not opcion.isdigit():
                print("Entrada inválida. Debe ingresar un número.")
                continue

            opcion_num = int(opcion)

            if opcion_num < 1 or opcion_num > len(disponibles_no_seleccionados):
                print("Opción inválida.")
                continue

            tipo_seleccionado = disponibles_no_seleccionados[opcion_num - 1].lower()

            while True:
                print(f"\nPara dispositivos tipo '{disponibles_no_seleccionados[opcion_num - 1]}':")
                print("A. Encender")
                print("B. Apagar")
                print("C. Sin cambiar")
                accion_input = input("Seleccione una opción (A/B/C): ").upper()

                acciones_map = {'A': 'e', 'B': 'a', 'C': 's'}

                if accion_input in acciones_map:
                    accion = acciones_map[accion_input]
                    acciones_por_tipo[tipo_seleccionado] = accion
                    tipos_seleccionados.add(tipo_seleccionado)

                    if tipo_seleccionado == "aire acondicionado" and accion == "e":
                        print("Seleccione el modo del aire acondicionado:")
                        print("A. Frío")
                        print("B. Calor")
                        modo_input = input("Seleccione una opción (A/B): ").upper()

                        modo_map = {'A': 'Frío', 'B': 'Calor'}
                        modo = modo_map.get(modo_input, 'Frío')

                        while True:
                            temp_input = input("Ingrese la temperatura (16 a 30): ").strip()
                            if not temp_input.isdigit():
                                print("Entrada inválida. Debe ingresar un número.")
                                continue
                            temperatura = int(temp_input)
                            if 16 <= temperatura <= 30:
                                break
                            else:
                                print("Temperatura fuera de rango.")

                        configuracion_aires["modo"] = modo
                        configuracion_aires["temperatura"] = temperatura

                    break
                else:
                    print("Opción inválida, seleccione A, B o C.")
