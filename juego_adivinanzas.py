from random import randint

print('*** Juego de Adivinanzas ***')

numero_secreto = randint(1,50)
intentos = 0
adivinanza = None
intentos_max = 5

while adivinanza != numero_secreto and intentos < intentos_max:
    adivinanza = int(input('Adivina el numero secreto (1-50): '))
    # Agregamos una ayuda para orientar al jugador
    if adivinanza < numero_secreto:
        print('El numero secreto es mayor.')
    elif adivinanza > numero_secreto:
        print('El numero secreto es menor.')
    # Incrementamos la variable de intentos
    intentos += 1

if adivinanza == numero_secreto:
    print(f'Felicidades, adivinaste el numero secreto en: {intentos} intentos.')
else:
    print(f'Lo siento, haz agotado el numero de intentos')
    print(f'El numero secreto era: {numero_secreto}')