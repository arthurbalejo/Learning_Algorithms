# faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. o programa sera interrompido quando o numero solicitado for negativo

numero = 0

while numero >= 0:
    numero = int(input('Insira um valor positivo para ver a tabuada: '))
    if numero < 0:
        print('PROGRAMA TABUADA ENCERRADO!')
        break
    else:
        print('-'*20)
        for c in range(1, 11):
            n = numero * c
            print(f'{numero} x {c} = {n}')
    print('-'*20)