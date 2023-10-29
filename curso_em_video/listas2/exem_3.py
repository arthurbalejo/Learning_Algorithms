galera = list()
#lista que pega os dados temporariamente
dado = list()

contMaior = 0
contMenor = 0
for c in range(0,3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade: ')))
    #dado[:] significa que vai adicionar uma copia da lista dado na lista galera
    galera.append(dado[:])
    dado.clear()

#printar so as pessoas maiores de 21 anos

for elemento in galera:
    if elemento[1] >= 21:
        print(f'nome: {elemento[0]} eh maior de idade')
        contMaior += 1
    else:
        print(f'nome: {elemento[0]} eh menor de idade')
        contMenor +=1

print(f'total maior de idade: {contMaior} e menor: {contMenor}')