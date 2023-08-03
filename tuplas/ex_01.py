#Tuplas são imutáveis, listas não
#lista = []
#tupla = ()
vendas = ('Lira','25/08/2020','15/02/1994',2000,'Estagiário')
nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(vendas)

print('nome: ',nome)
print('data_contratacao: ', data_contratacao)
print('data_nascimento: ', data_nascimento)
print('salario: ', salario)
print('cargo: ', cargo)

for item in enumerate(vendas):
    # print(item)

    i,vendas = item
    print(i)
    print(vendas)