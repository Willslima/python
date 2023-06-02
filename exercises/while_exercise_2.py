n = 0
n_list = []
n_sum = 0
option = 's'

while option != 'n':
    n = input('Type a number: \n')
    option = input('Add more a number ? s/n  ')
    n = int(n)
    n_sum += n

print('Total: ', n_sum)

# Dada uma lista de números inteiros, escreva um programa que calcula a soma de
# todos os números na lista
# Se preferir, pode utilizar a lista abaixo como exemplo:
# lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser = 100

pre_list = [1, 10, 20, 35, 22, 12]
n_b = 0
n_b_sum = 0

while n_b < len(pre_list):
    n_b_sum += pre_list[n_b]
    n_b += 1
print('Total of sum:',n_b_sum)