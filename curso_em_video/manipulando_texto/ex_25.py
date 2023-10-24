#receba um nome e veja se ele contem o sobrenome silva
nome = str(input("Insira o nome: ")).strip().title()
print("seu nome tem silva? {}".format('Silva' in nome))