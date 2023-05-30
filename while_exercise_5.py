# Exercícios – Estruturas de dados2# Alunos e suas notas representados através de dicionários

students = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

# Escreva uma programa que calcula a média das notas de todos os alunos.
note = 0

for student in students:
    note += student['nota']
print('The average is:',note // len(students))