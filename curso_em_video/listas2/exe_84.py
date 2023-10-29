# faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. no final, mostre:
# A) quantas pessoas foram cadastradas.
# B) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas mais leves

lista = list()
cadastro = list()
maior = menor = 0

while True:
    lista.append(str(input('insira o nome:')))
    lista.append(float(input('insira o peso:')))
    if len(cadastro) == 0:
        maior = lista[1]
        menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    cadastro.append(lista[:])
    lista.clear()
    condicao = str(input('tu deseja cadastrar mais pessoas? [S/N] ')).strip().lower()
    if condicao == 'n':
        break

print(f'A) quantas pessoas foram cadastradas? {len(cadastro)}')
print(f'B) uma listagem com as pessoas mais pesadas {maior}')
for pessoas in cadastro:
    if pessoas[1] == maior:
        print(f'{pessoas[0]}')
        break
print(f'C) uma listagem com as pessoas mais leves {menor}')
for pessoas in cadastro:
    if pessoas[1] == menor:
        print(f'{pessoas[0]}')
        break


print(cadastro)