print('*** Sistema de Administracion de Cuentas ***')

salir = False

while not salir:
    print(f'''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Escoge una opcion: '))
    if opcion == 1:
        print('Creando tu cuenta... \n')
    elif opcion == 2:
        print('Eliminando tu cuenta... \n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto\n')
        salir = True
    else:
        print('Opcion invalida')
else:  # Este else es opcional
    print('Terminando el sistema de Administracion de Cuentas')