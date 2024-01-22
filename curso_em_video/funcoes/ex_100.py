import random
#faça um programa que tenha um alista chamada numeros e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

def sorteia():
    lista = []
    for i in range (6):
        s = random.randint(0, 11)
        lista.append(s)
    return(lista)

def somaPar(lista):
    for i in lista:
        soma = 0
        if i % 2 == 0:
            soma += i
    return(soma)


print(somaPar(sorteia()))



