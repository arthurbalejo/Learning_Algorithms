estado = dict()
brasil = list()

for c in range(0, 3):
    estado ['uf'] = str(input('Unidade Federativa: '))
    estado ['sigla'] = str(input('Sigla do Estado: '))
    #no dicionario nao pode usar [:] fatiamento
    brasil.append(estado.copy())

for e in brasil:
    print(e)

print('*'*30)

for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')

print('*'*30)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()