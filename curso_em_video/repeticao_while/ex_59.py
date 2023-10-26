from time import sleep
# cire um programa que leia dois valores e mostre um menu na tela:

# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa

# seu programa devera realizar a operacao solicitada em cada caso

v1 = float(input("insira o primeiro valor: "))
v2 = float(input("insira o segundo valor: "))
menu = 0

resultado = 0

while menu != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')

    menu = int(input())

    if menu == 1:
        resultado = v1 + v2
        print('resultado eh: {}'.format(resultado))
        
    elif menu == 2:
        resultado = v1 * v2
        print('resultado eh: {}'.format(resultado))
        
    elif menu == 3:
        if v1 > v2:
            resultado = v1
        elif v1 < v2:
            resultado = v2
        else:
            resultado = v2
        print('resultado eh: {}'.format(resultado))
        
    elif menu == 4:
        v1 = float(input("insira o primeiro valor: "))
        v2 = float(input("insira o segundo valor: "))
    elif menu == 5:
        print('terminando programa')
    else:
        print('digite uma opcao valida')
    print('=-=' * 10)
    sleep(1)
print('fim do programa')