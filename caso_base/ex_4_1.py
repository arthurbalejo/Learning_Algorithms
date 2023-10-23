#escrever código da função soma



def soma_recursiva(lista):
    soma = 0
    for x in lista:
        if not lista:
            return 0
        else:
            x = lista.pop()
            return x + soma_recursiva(lista)
        
lista = [4, 5, 2, 8, 9]
print(soma_recursiva(lista))