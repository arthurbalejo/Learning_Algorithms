# crie um programa que vau ler varios numeros e colocar em uma lista.
# depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares sigitados, respectivamente.
# ao final, mostre o conteudo das tres listas geradas.

listaUm = []

while True:
    numero = int(input('Insira um numero: '))
    listaUm.append(numero)
    condicao = str(input('gostaria de inserir novamente? [S/N] ')).lower()
    if condicao == 'n':
        break

listaPar = []
listaImpar = []

for num in listaUm:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print('COMPLETA')
print(listaUm)
print('PAR')
print(listaPar)
print('IMPAR')
print(listaImpar)
