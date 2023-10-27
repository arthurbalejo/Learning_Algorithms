# crie um programa que tenha uma tupla com varias palavras (nao usar acentos). depois disso, voce deve mostrar, para cada palavra, quais sao suas vogais

palavras = 'gremio', 'acetona', 'fiasco', 'amanha'

for elemento in palavras:
    print(f'\n{elemento}:',end='')
    for letra in elemento:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')