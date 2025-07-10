print('*** Cajero Automatico ***')

salir = False
saldo = 1000

while not salir:
    print('''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoge una opcion: '))

    if opcion == 1:
        print(f'Tu saldo actual es: {saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        if retiro > saldo:
            print(f'No cuenta con el saldo suficiente. Saldo actual: {saldo}\n')
        else:
            saldo -= retiro # saldo = saldo - retiro
            print(f'Tu nuevo saldo es: {saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito # saldo = saldo + deposito
        print(f'Tu nuevo saldo es: {saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del cajero automatico, hasta pronto!')
        salir = True
    else:
        print('Opcion incorrecta')
else: print('Terminando la aplicacion de Cajero Automatico')


