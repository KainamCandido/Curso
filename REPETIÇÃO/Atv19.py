var_str = input("Digite o seu nome:")
for i in range(len(var_str)):
    print("a letra" , i , "do seu nome é :", var_str[i])


nome = input("Digite seu nome:")
r = int(input('Quantas vezes deseja repetir o nome?:'))
for c in range(r):
    print(nome)

for i in range (1,11):  # % = é resto de divisão
    if i % 2 == 0:
        print(i,'é par')
    else:
        print(i,'numero é impar')

x = 0
for i in range (1,6):
    x = x + i
    print(f'numero {x}')