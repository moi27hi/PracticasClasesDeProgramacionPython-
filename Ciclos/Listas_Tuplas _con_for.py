colores = ['Rojo','Azul','Verde','Amarillo']

print('--- LISTADO DE COLORES---')


for color in colores:
    print(f'-{color}.')
    
    
# Omitir ejecuciones en el codigo. 

print('*** \n Omitir ejecuciones de codigo**')

for color in colores:
    if color == 'Azul' or color == 'Verde':
        print(f'Se ha saltado este valor')
        continue
        
    print(f' -Color {color}.')
    

# Terminar el bucle antes de tiempo. 
print('*** \n Terminar el bucle antes de tiempo**')
for color in colores:
    if color == 'Amarillo':
        print('Se ha roto la ejecucion del bucle')
        break
    print(f' -Color {color}.')

    
        
    
    
       
    