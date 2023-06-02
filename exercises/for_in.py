names = ['will','lari','lena','bob'] #typle

for name in names:
    print(name)

numbers = {1,2,3,4,5} #sets/conjuntos

for number in numbers:
    print(number)

dictionary = { #dictionary
    'will':29,
    'lari':25,
    'lena':1.11,
    'bob':3
}

for data in dictionary:
    print(data)#return key
    print(dictionary[data]) #return value


for data in dictionary.items():
    print(data)

for data in dictionary.keys():
    print(data)

for k, v in dictionary.items():
    print('key', k, 'value', v)


