# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
# A)quantas vezes apareceu o valor 9
# B) em que posiçao foi digitado o primero valor 3
# C)quais foram os numeros pares


tupla = (int(input('insira um valor: ')),
int(input('insira um valor: ')),
int(input('insira um valor: ')),
int(input('insira um valor: ')))

print(f'A)quantas vezes apareceu o valor 9: {tupla.count(9)}')
print(f'B) em que posiçao foi digitado o primero valor 3: {tupla.index(3)}')
print('os valores pares digitados foram: ',end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end = ' ')
