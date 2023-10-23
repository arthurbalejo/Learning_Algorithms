#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas e minusculas
#quantas letras ao todo(sem considerar os espaços)
#quantas letras tem o primeiro nome

nome = str(input("insira teu nome completo: "))

print("nome maiusculo: {}".format(nome.upper()))
print("nome minuculo: {}".format(nome.lower()))

nomeSemEspaco = nome.replace(' ', '')

print("numero total de letras: {}" .format(len(nomeSemEspaco)))

nomeDividido = nome.split()

print("o primeiro nome e {} e possui {} letras".format(nomeDividido[0], len(nomeDividido[0])))

