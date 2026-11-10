qntd_mulher70 = 0
peso_masc = 0
quant_hm = 0
peso_total = 0

for c in range(6):
    sexo =input('Digite o sexo da pessoa (M OU F):').upper()
    peso =float(input('Digite o peso da pessoa:'))
    peso_total = peso_total + peso

    if sexo == 'M':
        quant_hm = quant_hm + 1
        peso_masc = peso_masc + peso

    elif sexo == 'F' and peso > 70:
        qntd_mulher70 = qntd_mulher70 + 1

    if quant_hm > 1:
        media_masc = peso_masc / quant_hm
        print(f'A media de peso entre os homens é {media_masc:.2f}')

print(f'O peso total do grupo é {peso_total:.2f}')
print(f'A quantidade de mulheres acima de 70 Kg é {qntd_mulher70}')