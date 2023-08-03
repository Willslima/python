email = 'williansantos38@gmail.com'
numero = 1000

#alinhamento de texto
print('Meu email é {:^50}, show?'.format(email))
print('Meu email é {:<50}, show?'.format(email))
print('Meu email é {:>50}, show?'.format(email))
print('Meu email é {}, show?'.format(email))

print('O número é: {:+}'.format(numero))
print('O número é: {:,}'.format(numero))
print('O número é: {:_}'.format(numero))
print('O número é: {:.2f}'.format(numero)) #número de casas decimais

custo = 5000
faturamento = 27000

lucro = faturamento - custo

lucro_texto = 'R${:_.2f}'.format(lucro)
print(lucro_texto.replace('.',',').replace('_','.')) #padrão brasileiro
