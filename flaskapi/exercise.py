palavra = 'banana'
letras = []
for letra in palavra:
    letras.append(letra)

thisdict = {}

for let in letras:
    if thisdict.get(let) == None:
        thisdict[let] = 1
    else:
        thisdict[let] += 1
    
print(thisdict)
