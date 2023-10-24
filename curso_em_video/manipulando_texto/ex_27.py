#faca um progra,a que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input("Insira teu nome completo: ")).strip().title()

nomeSeparado = nome.split()

print("Seu primeiro nome eh: {}".format(nomeSeparado))

print("Seu primeiro nome eh: {}".format(nomeSeparado[0]))

print("Seu ultimo nome eh: {}".format(nomeSeparado[len(nomeSeparado)-1]))

