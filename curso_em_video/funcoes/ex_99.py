#faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros.
#seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(lista):
    n = 0
    for i in lista:
        if i > n:
            n = lista[i]
    return n
lista = [1,2,4,5,6]

print(maior(lista))
