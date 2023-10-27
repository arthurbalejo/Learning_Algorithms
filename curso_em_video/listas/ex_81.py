# crie um programa que vai oer varios numeros e colocar em uma lista.
# depois disso, mostre:
# A) quantos numeros foram digitados.
# B) a lista de valores prdenada de forma decrescente
# C) se o valor foi 5 digitado e esta ou nao na lista

lista = []
count = 0

while True:
    numero = int(input('Insira um numero: '))
    lista.append(numero)
    count += 1
    condicao = str(input('Gostaria de inserir novamente? [S/N]')).strip().lower()
    if condicao == 'n':
        break

lista.sort(reverse = True)
print(lista)
print(f'foram digitados {count} numeros')

if 5 in lista:
    print('numero 5 faz parte da lista')
else:
    print('numero 5 nao faz parte da lista')