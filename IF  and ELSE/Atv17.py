# Alcool = 6.29
# Gasolina = 6.89

Comb =input('Qual Combustivel deseja abastecer?:').lower()
Litros = float(input("Quantos litros deseja?:"))

if Comb == 'a':
    if Litros <= 20:
        VLitros = 6.29 * Litros
        Desconto = VLitros * 0.03
        DescontoTotal = VLitros - Desconto
        print(f'Voce economizou R${((6.29 * 0.03)*Litros):.2f}')    
    elif Litros > 20 :
        VLitros = 6.29 * Litros
        Desconto = VLitros * 0.05
        DescontoTotal = VLitros - Desconto
        print(f'Voce economizou R${((6.29 * 0.05)*Litros):.2f}')

elif Comb == 'g':
    if Litros <= 20:
        VLitros = 6.89 * Litros
        Desconto = VLitros * 0.04
        DescontoTotal = VLitros - Desconto      
        print(f'Voce economizou R${((6.89 * 0.04)*Litros):.2f}')    
    elif Litros > 20 :
        VLitros = 6.89 * Litros
        Desconto = VLitros * 0.06
        DescontoTotal = VLitros - Desconto
        print(f'Voce economizou R${((6.89 * 0.06)*Litros):.2f}')

else:
       print('Inavalido')

print(f'o preço foi de R${DescontoTotal:.2f}')

# (  :.2f  ) - Serve para deixa somente 2 Numeros apos a virgula

