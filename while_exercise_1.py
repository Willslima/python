n = 0
n_list = []

while n >= 0:
    n = input('Type a number:\n')
    n = int(n)
    if n >= 0:
        n_list.append(n)

print(n_list)

# Escreva um programa que lê números inteiros positivos do usuário, um após o
# outro, e monta uma lista a partir desses números e depois imprime a lista montada.
# O programa deve continuar solicitando por números até que o elemento digitado
# seja um número negativo (que não deve ser inserido na lista).