Peso = float(input('Qual o peso do peixe pescado?:'))

if Peso > 50 :
    multa = (Peso- 50) * 4
    print(f'Você pagara uma multa de {multa}!')
else:
    print(f'Você não pagara uma multa')
