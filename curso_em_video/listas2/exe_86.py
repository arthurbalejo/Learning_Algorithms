#crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
#no final, mostre a matriz na tela, com a formatacao correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'insira um valor linha[{l}] coluna[{c}]: '))

for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
