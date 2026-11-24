from Gimnasio import Socio, Gimnasio

gym = Gimnasio("Space Gym")

socio1 = Socio("45123456", "Santino Berone", "Musculacion", 5)
socio2 = Socio("38987654", "Bautista Taborda", "Crossfit", 0)
gym.setSocio(socio1)
gym.setSocio(socio2)

def menu():
    print()
    print()
    print("1. Registrar nuevo socio")
    print("2. Registrar ingreso (Restar dia)")
    print("3. Ver socios activos")
    print("4. Ver socios inactivos")
    print("5. Consultar informacion de un socio (por DNI)")
    print("6. Ver estado general del gimnasio")
    print("7. Salir")
    print()
    print()
    
    op = int(input("Ingrese una opcion: "))
    return op


while True:

    op = menu()

    if op == 1:
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombre y Apellido: ")
        membresia = input("Ingrese tipo de membresia (Musculacion/Crossfit/General): ")
        try:
            dias = int(input("Ingrese dias disponibles: "))
            nuevo_socio = Socio(dni, nombre, membresia, dias)
            gym.setSocio(nuevo_socio)
        except ValueError:
            print("Los dias deben ser un numero entero.")

    elif op == 2:
        dni = input("Ingrese el DNI del socio: ")
        gym.darIngreso(dni)

    elif op == 3:
        gym.getActivos()

    elif op == 4:
        gym.getInactivos()

    elif op == 5:
        dni = input("Ingrese el DNI a buscar: ")
        encontrado = False
        for s in gym.socios:
            if s.dni == dni:
                s.getInfo()
                encontrado = True
        if not encontrado:
            print("No se encontro ningun socio con ese DNI.")

    elif op == 6:
        gym.getEstadoGeneral()

    elif op == 7:
        break
    else:
        print("No elegiste ninguna opcion fraca")
                    
