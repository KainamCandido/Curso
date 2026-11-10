letra = input('Digite uma letra para saber seu tipo:').lower()

if letra in '1234567890' :
    print('isso é um numero')
else:
    if letra== 'a' or letra=='e'or letra=='i'or letra== 'o' or letra=='u':
        print('A letra é uma vogal' )
        if letra== 'w':
            print('Letra w digitada')
    else:
        print('A letra é consoante')

# upper - transforma tudo escrito no input em maiusculo
# lower = transforma tudo escrito no input em minuscula

#{----------------------------------
# if letra in 'aeiou':
#     print('letra vogal')
# else:
#     print('Letra consoante')
# muito mais simples
# -----------------------------------