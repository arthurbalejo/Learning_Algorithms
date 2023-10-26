# crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
# depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla
import random

n1 = random.randint(0,100)
n2 = random.randint(0,100)
n3 = random.randint(0,100)
n4 = random.randint(0,100)
n5 = random.randint(0,100)

tupla = n1, n2, n3, n4, n5

print(tupla)

maior = n1
menor = n1

for c in range(len(tupla)):
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]

print(f'maior: {maior}')
print(f'menor: {menor}')