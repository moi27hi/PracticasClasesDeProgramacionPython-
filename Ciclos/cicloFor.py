# Bucle for 

for i  in ['Ana','Juan','Carlos','Esteban','Eduardo']:
    print(f'Hola ... {i}')


for i in [1,2,3,4,5]:
    print('\nHola mundo')


for i in [2, 10,3,4,'Alejandro']:
    print(f'Elemento: {i}')


# Creando listas desde una variable exterior. 

print('\nCiclo for con una variable exterior')

coleccion = [2, 10,3,4,'Alejandro']

for i in coleccion:
    print(f'Elemento: {i}')

# Usando for en diccionarios. 
print('\n***Ciclo for con diccionarios***')

coleccion = {'Alejandro': 22, 'Maria':23, 'Jose':45, 'Luis':22}

for i in coleccion:
    print(f'{i} -> {coleccion[i]}')


print('***\nOtro metodo para trabajar con diccionarios***')
for clave, valor in coleccion.items():
    print(f'{clave} -> {valor}')


# para recorrer cadenas. 

print('\n*** Recorriendo cadenas***')

coleccion = 'Alejandro'

for i in coleccion:
    print(f'{i} ', end= '-') # para imprimir las letras dentro de la misma lines









