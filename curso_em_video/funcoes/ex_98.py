#faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.
#seu programa tem que realizar tres contagens atraves da função criada
#a) de 1 ate 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

def contador(inicio, fim, passo):
    if inicio >= fim:
        while inicio > fim:
            print(inicio)
            inicio -= passo
    if inicio <= fim:
        while inicio <= fim:
            print(inicio)
            inicio += passo

i = 10
f = 1
p = 1

contador(i, f, p)