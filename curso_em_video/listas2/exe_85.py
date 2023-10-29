#crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. no fina, mostre os valores pares e impares em ordem crescente.

lista = [[],[]]
preLista = 0

for _ in range(1, 8):
    preLista = int(input(f'Insira o valor n{_}: '))
    if preLista % 2 == 0:
        lista[0].append(preLista)
    else:
        lista[1].append(preLista)

lista[0].sort()
lista[1].sort()
print(f'os valores pares em ordem crescente: {lista[0]}')
print(f'os valores impares em ordem crescente: {lista[1]}')