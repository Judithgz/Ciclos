print('*** Dibujar Triangulo Simetrico ***')

filas = int(input('Proporciona el numero de filas: '))

# Iterar sobre cada fila del triangulo
for fila in range(1,filas+1):
    espacios_blanco = ' ' * (filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{asteriscos}')