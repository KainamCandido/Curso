Soma = 0
num1 =int(input('Digite um numero:'))
num2 = int(input('Digite o ultimo numero:'))

if  num1 < num2 :
    for c in range (num1 ,num2):
        print(c)
        Soma = Soma + c
if  num1 > num2 :
    for c in range (num2 -1,num1):
        print(c)
        Soma = Soma + c
print(f'A soma dos numeros entre os valores é {Soma}')    