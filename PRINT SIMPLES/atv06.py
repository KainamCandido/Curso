Ganho_hora = float(input('Quanto você recebe por hora?:'))
horas_trabalhadas = float(input('Quantas horas vc trabalha num dia?:'))
dias_trabalhados = int(input('Quantos dias vc trabalha?:'))

mês = horas_trabalhadas * dias_trabalhados
Salario = Ganho_hora * mês

print(f'você ganha R${Salario} por mês')

