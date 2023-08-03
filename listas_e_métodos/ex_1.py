lista = ['Will','Willian','WillSlima']
lista2 = ['Lari','Larissa','Lux']
lista3 = ['Helena', 'Lena', 'Gordinha']

todas_listas = [lista, lista2, lista3]

print(todas_listas)

print('meu nome é {}, minha esposa é a {} e nossa filha é a {}'.format(lista[1], lista2[1], lista3[0]))

# nome = input('Digite o seu nome: ')

# if nome in lista:
#     print('O nome está na lista')
# else:
#     lista.append(nome)
#     print('Nome adcionado à lista',lista)

try:
    lista.remove('willian')
except:
    print('Por algum motivo não foi possível remover o nome da lista')

print('\n'.join(lista))

lst1 = ['apple tv','mac','iphone x','Ipad','apple watch','mac book','airpods']
lst2 = lst1.copy() #Mantém a lista 2 imutável.
lst1[2] = 'iphone 12'

print(lst1)
print(lst2)

vendedores = ['Lira','João','Diego','Alon']
produtos = ['ipad','iphone']
vendas = [[100,200],[300,500],[50,1000],[900,10]]

