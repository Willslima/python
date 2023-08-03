palavras = []
palavra = input('Digite a palavra para inserir na lista. \n Digite exit para sair: ')
while palavra != 'exit':
    palavras.append(palavra)
    palavra = input('Digite a palavra para inserir na lista. \n Digite exit para sair: ')

print(palavras)