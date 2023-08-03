preco_produtos = [100,150,300,5500]
produtos = ['vinho','cafeteira','microondas','iphone']

#S/ list comprehension
impostos = []
for item in preco_produtos:
    impostos.append(item * 0.3)
print(impostos)

impostos2 = [preco * 0.3 for preco in preco_produtos]
print(impostos2)