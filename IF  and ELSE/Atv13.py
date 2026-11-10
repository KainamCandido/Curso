Nota1 = float(input('Digite a primeira nota do aluno:'))
Nota2 = float(input('Digite a segunda nota do aluno:'))

media = (Nota1 + Nota2) /2
if media == 10 or media >10:
    print('aprovado com distinção')
elif media >=7:
    print('Aprovado')
elif media >=3 and media <7: 
    print('recuperação')
else:
    print('reprovado')

