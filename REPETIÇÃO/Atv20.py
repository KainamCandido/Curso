total_compra = 0
for c in range(3):
    nome= input('Nome produto:')
    valor= float(input('Valor:R$ '))
    total_compra = total_compra + valor

if total_compra >= 1.000:
    total_des =  total_compra * 0.85
    print(f'Total da compra com desconto: R${total_des}')
else:
    print(f'Total a pagar: RS${total_compra}')

