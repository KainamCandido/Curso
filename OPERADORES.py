a = 10
b = 3

soma = a + b              # Adição
subtracao = a - b         # Subtração
multiplicacao = a * b     # Multiplicação
divisao = a / b           # Divisão (resultado é sempre float)
divisao_inteira = a // b  # Divisão inteira (descarta a parte decimal)
modulo = a % b            # Módulo (resto da divisão)
potencia = a ** b         # Potenciação



print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao:.2f}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")