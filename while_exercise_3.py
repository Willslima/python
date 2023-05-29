# Data uma lista de números inteiros, escreva um programa que calcula a média dos
# números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
# deve imprimir apenas 12 .
# Se preferir, pode utilizar a lista abaixo como exemplo:
# lista = [1, 10, 20, 35, 22, 12]

list = [1, 10, 20, 35, 22, 12]
n = 0
n_sum = 0

while n < len(list):
    n_sum += list[n]
    n += 1
n_sum = n_sum / len(list)
print(int(n_sum))