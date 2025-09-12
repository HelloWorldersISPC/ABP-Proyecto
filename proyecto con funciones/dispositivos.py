def listar_dispositivos(dispositivos):
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return
    print("Dispositivos:")
    for i, disp in enumerate(dispositivos, 1):
        estado_texto = "Encendido" if disp["estado"] else "Apagado"
        linea = f"{i}. {disp['nombre']} - {disp['ubicacion']} - {disp['tipo']} - Estado: {estado_texto}"
        
        if disp["tipo"].lower() == "aire acondicionado" and disp["estado"]:
            modo = disp.get("modo", "No definido")
            temperatura = disp.get("temperatura", "No definida")
            linea += f" - Modo: {modo} - Temp: {temperatura}°C"

        print(linea)

def agregar_dispositivo(dispositivos, rol_actual, escenarios):
    tipos = ["Luz", "Cámara", "Aire acondicionado", "Lavarropa"]
    ubicaciones = [
        "Patio", "Frente de la casa", "Dormitorio principal", "Dormitorio huéspedes",
        "Lavadero", "Living", "Comedor", "Baño", "Cocina", "Oficina"
    ]

    while True:
        print("Seleccione el tipo de dispositivo:")
        for i, tipo in enumerate(tipos, 1):
            print(f"{i}. {tipo}")
        print("0. Volver al menú principal")

        tipo_input = input("Ingrese el número del tipo: ")
        if not tipo_input.isdigit():
            print("Entrada inválida. Debe ser un número.")
            continue

        tipo_opcion = int(tipo_input)
        if tipo_opcion == 0:
            if rol_actual == "admin":
                from menu import menu_administrador
                menu_administrador(dispositivos, escenarios)
            elif rol_actual == "invitado":
                from menu import menu_invitado
                menu_invitado(dispositivos, escenarios)
            return
        if tipo_opcion < 1 or tipo_opcion > len(tipos):
            print("Opción inválida para tipo.")
            continue

        tipo_seleccionado = tipos[tipo_opcion - 1]
        break

    while True:
        print("\nSeleccione la ubicación del dispositivo:")
        for i, ubicacion in enumerate(ubicaciones, 1):
            print(f"{i}. {ubicacion}")
        print("0. Volver al menú principal")

        ubicacion_input = input("Ingrese el número de la ubicación: ")
        if not ubicacion_input.isdigit():
            print("Entrada inválida. Debe ser un número.")
            continue

        ubicacion_opcion = int(ubicacion_input)
        if ubicacion_opcion == 0:
            if rol_actual == "admin":
                from menu import menu_administrador
                menu_administrador(dispositivos, escenarios)
            elif rol_actual == "invitado":
                from menu import menu_invitado
                menu_invitado(dispositivos, escenarios)
            return
        if ubicacion_opcion < 1 or ubicacion_opcion > len(ubicaciones):
            print("Opción inválida para ubicación.")
            continue

        ubicacion_seleccionada = ubicaciones[ubicacion_opcion - 1]
        break

    nombre = input("Ingrese un nombre para el dispositivo (o '0' para volver al menú principal): ").strip()
    if nombre == "0":
        if rol_actual == "admin":
            from menu import menu_administrador
            menu_administrador(dispositivos, escenarios)
        elif rol_actual == "invitado":
            from menu import menu_invitado
            menu_invitado(dispositivos, escenarios)
        return

    dispositivo = {
        "tipo": tipo_seleccionado,
        "ubicacion": ubicacion_seleccionada,
        "nombre": nombre,
        "estado": True,  # Por defecto, el dispositivo se agrega encendido
    }
    dispositivos.append(dispositivo)
    print(f"Dispositivo '{nombre}' ({tipo_seleccionado}) agregado en '{ubicacion_seleccionada}'.")

    if rol_actual == "admin":
        from menu import menu_administrador
        menu_administrador(dispositivos, escenarios)
    elif rol_actual == "invitado":
        from menu import menu_invitado
        menu_invitado(dispositivos, escenarios)


def eliminar_dispositivo(dispositivos):
    if not dispositivos:
        print("No hay dispositivos para eliminar.")
        return

    while True:
        print("\nDispositivos disponibles:")
        for i, dispositivo in enumerate(dispositivos, start=1):
            print(f"{i}. {dispositivo['nombre']} - {dispositivo['tipo']} - Estado: {dispositivo['estado']}")
        print("0. Volver al menú principal")

        opcion = input("Seleccione el número del dispositivo a eliminar: ")

        if opcion == '0':
            break

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(dispositivos):
            print("Opción inválida. Intente de nuevo.")
            continue

        indice = int(opcion) - 1
        dispositivo_eliminado = dispositivos.pop(indice)
        print(f"Dispositivo '{dispositivo_eliminado['nombre']}' eliminado correctamente.")
        break

def usar_dispositivo(dispositivos):
    if not dispositivos:
        print("No hay dispositivos disponibles.")
        return

    while True:
        print("\nDispositivos:")
        for i, dispositivo in enumerate(dispositivos, 1):
            estado_texto = "Encendido" if dispositivo["estado"] else "Apagado"
            extra_info = ""
            if dispositivo["tipo"] == "Aire acondicionado" and dispositivo["estado"]:
                modo = dispositivo.get("modo", "Sin asignar")
                temp = dispositivo.get("temperatura", "Sin asignar")
                extra_info = f" | Modo: {modo} | Temp: {temp}°C"
            print(f"{i}. {dispositivo['nombre']} - {dispositivo['ubicacion']} - {dispositivo['tipo']} - Estado: {estado_texto}{extra_info}")
        print("0. Volver al menú principal")

        opcion_input = input("Seleccione el número del dispositivo para usar: ")
        if not opcion_input.isdigit():
            print("Entrada inválida. Debe ingresar un número.")
            continue

        opcion = int(opcion_input)

        if opcion == 0:
            break

        if opcion < 1 or opcion > len(dispositivos):
            print("Opción inválida.")
            continue

        dispositivo = dispositivos[opcion - 1]

        while True:
            estado_texto = "Encendido" if dispositivo["estado"] else "Apagado"
            print(f"\nDispositivo '{dispositivo['nombre']}' - Estado actual: {estado_texto}")
            print("1. Encender")
            print("2. Apagar")
            print("0. Volver al menú anterior")

            accion = input("Seleccione una opción: ")

            if accion == '0':
                break
            elif accion == '1':
                if dispositivo["estado"]:
                    print(f"El dispositivo '{dispositivo['nombre']}' ya está encendido.")
                else:
                    dispositivo["estado"] = True
                    print(f"Dispositivo '{dispositivo['nombre']}' ahora está Encendido.")

                if dispositivo["tipo"] == "Aire acondicionado" and dispositivo["estado"]:
                    while True:
                        print("\nOpciones para el aire acondicionado:")
                        print("1. Cambiar modo (Frío o Calor)")
                        print("2. Cambiar temperatura")
                        print("3. Ver estado")
                        print("0. Volver al menú anterior")

                        opcion_aire = input("Seleccione una opción: ")

                        if opcion_aire == "0":
                            break
                        elif opcion_aire == "1":
                            print("\nSeleccione el modo:")
                            print("A. Frío")
                            print("B. Calor")
                            seleccion = input("Ingrese A o B: ").strip().upper()
                            if seleccion == "A":
                                dispositivo["modo"] = "Frío"
                                print("Modo actualizado a Frío.")
                            elif seleccion == "B":
                                dispositivo["modo"] = "Calor"
                                print("Modo actualizado a Calor.")
                            else:
                                print("Opción inválida.")
                        elif opcion_aire == "2":
                            nueva_temp_input = input("Ingrese nueva temperatura (16 a 30): ")
                            if not nueva_temp_input.isdigit():
                                print("Debe ingresar un número.")
                                continue
                            nueva_temp = int(nueva_temp_input)
                            if 16 <= nueva_temp <= 30:
                                dispositivo["temperatura"] = nueva_temp
                                print(f"Temperatura actualizada a {nueva_temp}°C.")
                            else:
                                print("Temperatura fuera de rango.")
                        elif opcion_aire == "3":
                            modo = dispositivo.get("modo", "Sin asignar")
                            temp = dispositivo.get("temperatura", "Sin asignar")
                            print(f"Modo: {modo}, Temperatura: {temp}°C")
                        else:
                            print("Opción no válida.")
                break

            elif accion == '2':
                if not dispositivo["estado"]:
                    print(f"El dispositivo '{dispositivo['nombre']}' ya está apagado.")
                else:
                    dispositivo["estado"] = False
                    print(f"Dispositivo '{dispositivo['nombre']}' ahora está Apagado.")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

