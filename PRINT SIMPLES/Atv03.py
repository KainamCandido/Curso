pot = 2**4
# o * representam o primeiro numero elevado ao segundo
#print(pot)
    
num = float(input("Digite um numero: "))

print('o numero informado foi', num, "parabéns")

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('terceira nota:'))
nota4 = float(input('Quarta nota:'))
media = (nota1 + nota2 + nota3 + nota4) /4 

print('Sua média foi :',media)
if media >=6:
    print('aprovado, parabéns')
else:
    print('reprovado,melhore')