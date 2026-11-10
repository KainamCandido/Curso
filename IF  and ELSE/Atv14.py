Prod1= float(input('Qual valor da pastel?: '))
Prod2= float(input('Qual valor do suco?: '))
Prod3= float(input('Qual valor do coxinha?: ' )) 

# Produto_do_meio
# Produto_mais__caro
# Produto_mais_barato

if Prod1 < Prod2 and Prod1 < Prod3:
    if Prod2< Prod3:
       print('1° pastel,2° suco,3°coxinha')
    if Prod3 < Prod2:
            print ('1° pastel,2° coxinha,3° suco')
if Prod2 < Prod1 and Prod2 < Prod3:
    if Prod1< Prod3:
            print('1° suco,2° pastel,3° coxinha')
    if Prod3< Prod2:
        print ('1° suco,2° coxinha,3° pastel')

if Prod3 < Prod1 and Prod3< Prod2:
    if Prod1< Prod2:
         print('1° coxinha,2° pastel ,3° suco')
    else:
        print ('1° coxinha,2° suco,3° pastel')


if Prod1 > Prod2 and Prod1 > Prod3:
        print('O produto mais caro é Pastel, nao recomendo a compra!')
elif Prod2> Prod1 and Prod2 > Prod3:
    print('Produto mais caro é suco ,nao recomendo a compra!')
else: 
    print('O produto mais caro é o Pastel ,nao recomendo a compra!')

# produto_mais_caro   