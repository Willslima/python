def calcular_parametro(*notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma 

print('Soma', calcular_parametro(3,3,3,3))
print('Soma', calcular_parametro(5,5))


#*args => múltiplos argumentos -- **kwargs =: argumentos com parametros arg['parametro']
def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

print('Preco:',preco_final(1000, desconto=0.1, imposto=0.3))