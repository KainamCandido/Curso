
p1 = input('Telefonou para a vitima :').upper()
if p1 == 'SIM':
    r1 = 1
elif p1=='NAO':
        r1 = 0
else:
    r1 = 6 

p2 = input('Esteve no local do crime ? :').upper()
if p2 == 'SIM':
    r2 = 1
elif p2=='NAO':
        r2 = 0
else:
    r2 = 6

p3 = input('Mora perto da vítima? :').upper()
if p3 == 'SIM':
    r3 = 1
elif p3=='NAO':
        r3 = 0
else:
    r3 = 6 

p4 = input('Devia para a vítima?:').upper()
if p4 == 'SIM':
    r4 = 1
elif p4=='NAO':
        r4 = 0
else:
    r4 = 6

p5 = input('Ja trabalhou para a vítima ?:').upper()
if p5 == 'SIM':
    r5 = 1
elif p5 == 'NAO':
        r5 = 0
else:
    r5 = 6
resp = r1 + r2 + r3 + r4 + r5

if resp < 2:
    print ('Inocente')
elif resp == 2:
    print('Suspeito')
elif resp == 3 or resp == 4:
    print('Cumplice')
elif resp == 5 :
    print('Culpado')
else:
    print('Invalido')