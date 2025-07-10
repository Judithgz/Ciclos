print('*** Calculadora en Python ***')

salir = False

while not salir:
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoge una opcion: '))
    # Solicitamos los numeros primero
    if 1 <= opcion <= 4:
        num1 = float(input('Da el valor 1: '))
        num2 = float(input('Da el valor 2: '))
    # Operacion a realizar
    if opcion == 1:
        resultado = num1 + num2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2:
        resultado = num1 - num2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3:
        resultado = num1 * num2
        print(f'El resultado de la multiplicacion es: {resultado}\n')
    elif opcion == 4:
        resultado = num1 / num2
        print(f'El resultado de la division es: {resultado}\n')
    elif opcion == 5:
        print('Saliendo del programa de Calculadora. Hasta pronto!')
        salir = True
    else:
        print('Opcion incorrecta')



