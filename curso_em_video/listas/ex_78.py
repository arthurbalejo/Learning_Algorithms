# faca um programa que leia 5 valores numericos e guarde-os em uma lista
# no final, mostre qual foi o maior e o menor valor digitado e as suas suas respectivas posicoes na lista

lista = []
maior = 0
menor = 0

for c in range(5):
    lista.append(int(input(f'Insira na posicao {c}: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'menor valor digitado: {menor} nas posicoes ',end='')

for c in range(5):
    if lista[c] == menor:
        print(f'{c}... ',end='')

print('\n')

print(f'maior valor digitado: {maior} nas posicoes ',end='')
for c in range(5):
    if lista[c] == maior:
        print(f'{c}... ',end='')
    

        

# 
# print(f'maior valor digitado: {max(lista)} na posicao {lista.index(max(lista))}')