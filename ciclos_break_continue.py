print('*** Break & Continue ***')

# Ejemplo con break
print('\nBreak')
for numero in range(1, 10):
    if numero % 2 == 0: # Numero par
        print(numero)
        break # Salimos del ciclo inmediatamente


# Ejemplo con continue
print('\nContinue')
for numero in range(1, 10):
    if numero % 2 == 1: # Numero impar
        continue
    print(numero) # numeros pares