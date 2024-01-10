#empacotador
def contador(*num):
    tam = len(num)
    print(f'recebi os valores {num} e sao ao todo {tam} numeros')

def soma(*num):
    s = 0
    for n in num:
        s += n
    print(f'a soma dos valores {num} eh: {s}')

#programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

soma(2, 1, 7)
soma(8, 0)
soma(4, 4, 7, 6, 2)