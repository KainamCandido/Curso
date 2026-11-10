Mais_velho = 0
D_menor = 0
idade_total = 0
nome_mais_velho = ''
for c in range (4):
    nome= input('Nome da pessoa:')
    idade =int(input('Idade da pessoa:'))
    sexo = input('Sexo da pessoa (M ou F ):').upper()  
    idade_total = idade_total + idade

    if sexo == 'F' and idade < 20:
        D_menor = D_menor +  1
    if sexo == 'M':
        if idade > Mais_velho:
            Mais_velho = idade
            nome_mais_velho = nome

media_idade = idade_total / 4


print(f'A media das idades das pessoas é :{media_idade:.2f}') 

print(f'Existem {D_menor} mulheres com idade menor que 20 anos')     

print(f'O homem mais velho é {nome_mais_velho} e tem : {Mais_velho}')