nome = input('olá digite seu nome:')
# usar "f" antes de uma string faz com que a variavel possa ser colocada no texto usando {} sem interferir no codigo

Raio = float(input (f'olá {nome} digite o raio do circulo que deseja calcular:'))
área = (3.1415 * (Raio**2))
print (f'a área do circulo é:{área}')

