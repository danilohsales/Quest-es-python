alunos = input().split()  
notas = input().split()   

for i in range(len(notas)):
    notas[i] = float(notas[i])

soma_notas = 0
for nota in notas:
    soma_notas += nota
media_turma = soma_notas / (len(alunos) * 2)

relatorio = []
# Iterate through students and their grades
for i in range(len(alunos)):
    # Calculate index for the current student's grades
    # index_notas = i * 2
    # Extract the grades of the current student
    nota1 = float(notas[i * 2])
    nota2 = float(notas[i * 2 + 1])
    
    # Calculate the average grade for the current student
    media_aluno = (nota1 + nota2) / 2
    
    # Check if the student's average grade is below the class average
    if media_aluno < media_turma:
        relatorio.append((nota1, nota2, media_aluno, alunos[i]))

# Print the report
for aluno in relatorio:
    print(f'- {aluno[0]:.1f} {aluno[1]:.1f} ({aluno[2]:.1f}) {aluno[3]}')

# Print the class average
print(f'> media turma: {media_turma:.2f}')
