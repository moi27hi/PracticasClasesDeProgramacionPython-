veces = int(input('Cuantos numeros desea ingresas? ')) #4 

cont = 0
acum = 0

for i in range(veces):
    print(f' --- ciclo  {str(i+1)} ---')
    num = int(input('Ingresa un numero: ')) #2

    if num%2==0:
        cont +=1 # cont = cont +1
    
    else:
        acum +=num  # acum = acum + num 
 
    
    
print(f'La cantidad de numeros pares es: {cont}')
print(f'La cantidad de numeros impares es: {acum} ')




