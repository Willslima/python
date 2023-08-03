mais_vendidos = {
    'tecnologia':'iphone',
    'refrigeracao':'ar consul 12000 btu',
    'livros':'O alquimista'
}

# Pegar item Dicionário e Verificar Item Dicionário

print(mais_vendidos['refrigeracao'])
print(mais_vendidos.get('refrigeracao'))

for setor, produto in mais_vendidos.items():
    print('Setor {}, produto {}'.format(setor, produto))

#adicionando itens de maneira diferentes.
mais_vendidos['games'] = 'ps4'
mais_vendidos.update({'pc':'4090'})

print(mais_vendidos)

#alteranado item existente, chaves não duplicam.
mais_vendidos['games'] = 'ps5'

print(mais_vendidos)

games = mais_vendidos.pop('games')

print(games)