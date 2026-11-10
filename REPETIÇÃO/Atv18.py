val1 = int(input('Deseja contar de que numero?:'))
val2 =int(input('Quer contar ate que numero?:'))
Pulos = int(input('Quer contar em que intervalo de numeros?:'))
for c in range(val1,val2+1, Pulos):
     #O primeiro numero é o começo,o segundo o limite, e o terceiro o intervalo  entre eles
    print(c)                       


for c in range(1,50+1,2):
    print(f'Mostre os numeros impares:{c}')

for c in range(10,0-1,-1):
    print(f'Contagem regressiva {c}')
print('Feliz,ano novo!!!!!!!')


