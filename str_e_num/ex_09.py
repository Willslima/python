faturamento = input('Qual foi o faturamento da loja esse mês? ')
custo = input('Quais foram os custos da loja esse mês? ')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de {} reais'.format(lucro))
else:
    print('Algum valor não foi fornecido')

    