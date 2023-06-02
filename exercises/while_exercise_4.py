# Suponha o seguinte programa:
# # Alunos e suas respectivas notas
# alunos = [
# ("Alice", 8),
# ("Bob", 7),
# ("Carlos", 9),
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

students = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]

i = 0
n_sum = 0

while i < len(students):
    n_sum += students[i][1]
    i += 1
    
print(n_sum // len(students))

