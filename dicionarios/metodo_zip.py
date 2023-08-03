produtos = ['iphone','samsung galaxy','tv samsung','ps5','tablet','ipad']
vendas = [15000,12000,10000,14300,1720,1000]

#cria tuplas
lista_tuplas = zip(produtos,vendas)
print(lista_tuplas)

for item in lista_tuplas:
    print(item)
#===================================================================================== Criando dicionário

produtos = ['iphone','samsung galaxy','tv samsung','ps5','tablet','ipad']
vendas = [15000,12000,10000,14300,1720,1000]

#cria tuplas
lista_tuplas = zip(produtos,vendas)
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)