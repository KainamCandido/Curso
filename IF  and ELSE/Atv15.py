dipi = 3.00
para = 3.50                          #ESSA FOI COMPLICADA
morfina = 9.99

print('PRODUTOS')
print('1 - DIPIRONA')
print('2 - PARACETAMOL')
print('3 - MORFINA')
print('')


Compra = input('Oque deseja comprar?: ')
if Compra == '1':
    Quantidade=int(input('Quantas cartelas deseja?: '))
    if Quantidade <= 0 :
        print('Compra invalida')
    elif Quantidade > 0:
        Compra = dipi * Quantidade
        if Compra >= 25 :
            Desconto= Compra * 0.15
            Compra_desconto = Compra - Desconto
            print(f'O valor da sua compra foi de {Compra_desconto}')
        else:    
            print(f'O valor da compra foi de {Compra}')
     

elif Compra == '2':
    Quantidade=int(input('Quantas cartelas deseja?: '))
    if Quantidade <= 0 :
        print('Compra invalida!')
    elif Quantidade > 0:
        Compra = para * Quantidade
        if Compra >= 30 :
            Desconto= Compra * 0.15
            Compra_desconto = Compra - Desconto
            print(f'O valor da sua compra foi de {Compra_desconto}')
        else: 
            print(f'O valor da compra foi de {Compra}')
        
elif Compra == '3':
    Receita=input('Você possui receita?:').lower()
    if Receita == 's':
        Quantidade=int(input('Quantas cartelas deseja comprar?:'))
        if Quantidade <= 0 :
            print('Compra invalida')
        elif Quantidade > 0:
            Compra = morfina * Quantidade
            if Compra >= 50 :
                Desconto= Compra * 0.15
                Compra_desconto = Compra - Desconto
                print(f'O valor da sua compra foi de {Compra_desconto}')  
            else :
                print(f'O valor da compra foi de {Compra}')
            
    elif Receita == 'n':
        print('Compra Recusada')
    else:
        print('Invalido')