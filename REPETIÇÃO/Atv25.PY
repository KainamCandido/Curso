print('INICIO')

x = None                      # != é diferente de...
while x != 'SAIR':
    x = input('digite uma palavra ou digite "sair" para cancelar o comando :').upper()

print('Cabou')

print('--='*10)

x = 0
while x <= 100 :
    print(f'Numero é:{x}')
    x = x + 1
print('ACABOU')

print('--='*10)

x = 10
while x >= 0 :
    print(f'Lançamento em :{x}')
    x = x -1
print('Fogo!!!')

print('--='*10)

i = None    
while i != 'Invalido':
    i = int(input('Digite um numero de 0 a 10:'))
    if i <0 or i >10 :
        i = 'Invalido'

print('Numero invalido')

print('--='*10)

nome = input('insira o nome do usuario:')
senha = input('insira a senha do usuario:')

while senha == nome:
    print('nome do usuario igual a senha,tente novamente:')
    nome = input('insira o nome do usuario:')
    senha = input('insira a senha do usuario:')
print(f'nome de usuario:{nome} senha do usuario {senha}')

print('--='*10)

nome = input('Digite um nome:')

while len(nome) < 3:
    print('Nome invalido')
    nome= input('Digite seu nome:')

idade = int(input('Digite sua idade:'))

while idade < 0 or idade > 150:
    print('Idade invalida')
    idade = int(input('Digite sua idade:'))

Salario = float(input ('Digite seu salario:'))

while Salario < 0 :
    print('Salario invalido')
    Salario = float(input('Digite seu salario:'))

Est_civil = input('Digite seu estado civil (s ou c ou v ou d):').lower()

while Est_civil != 's' and Est_civil != 'c'and Est_civil != 'v' and Est_civil != 'd':
    print('Estado civil Invalido')
    Est_civil = input('Digite seu estado civil (s ou c ou v ou d):').lower()


print(f'Seu nome é {nome} vc tem {idade} anos, Seu salario é {Salario} e seu estado civil é {Est_civil}:')

print('FIM')







