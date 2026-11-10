
media_geral = 0
maior_nota = 0
aluno_maior_media = ''
alunos_aprovados = 0

for i in range(5):
    media_aluno = 0  
    soma = 0
    aluno = input('Nome do aluno:')
    for c in range(4):
        nota = float(input('Qual as nota desse aluno:'))
        soma = soma + nota    
        media_aluno= soma / 4
    print(f'A media de {aluno} foi {media_aluno}')    

    if media_aluno >= 6:
        print(f'Aluno {aluno} aprovado')
        alunos_aprovados = alunos_aprovados + 1

    if media_aluno < 6:
            print(f'aluno {aluno} reprovado')

    if media_aluno > maior_nota:
        maior_nota = media_aluno
        aluno_maior_media = aluno

    media_geral = media_aluno + media_geral
    media_turma = media_geral / 5
             

print(f'A quantidade de alunos aprovados foram {alunos_aprovados}')        
print(f'A media da turma foi de {media_turma:.2f}')
print(f'A media geral foi de {media_geral}')
