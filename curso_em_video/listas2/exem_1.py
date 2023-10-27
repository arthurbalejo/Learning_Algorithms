teste = list()
teste.append('gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)