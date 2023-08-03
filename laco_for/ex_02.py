produtos = ['coca','pepsi','guaraná','sprite','fanta','mineirinho']

for item in produtos:
    print('Produção do {}'.format(item))

for i in range(11):
    print('=========================')
    for x in range(11):
        r = i*x
        print('{} x {} = {} ||'.format(i,x,r))