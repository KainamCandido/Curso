num1 = float(input("Digite um numero: "))
if num1 < 0:
    print("Numero negativo: ")
else:
    print('Numero postivo: ')

num1 = int(input('Digite um nummero: '))
num2 = int(input('Digite um numero: '))

# IF = se.
# ELSE = senão, deve ser colocado apenas no final.
# ELIF = para adicionar mais opções ,n tem limite.
# o elif deve ser colocado antes do else.
if num1 > num2:
    print(f'O número {num1} é maior.')
elif num1 == num2:
    print(f'Os numeros são iguais!!')
else:
    print(f'O número {num2} é menor.')
