#crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
#no final, mostre a matriz na tela, com a formatacao correta.
#aprimorar, mostrando:
# A) a soma de todos os valores pares digitados.
# B) a soma dos valores da terceira coluna
# C) o maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
somaB = 0
maiorC = 0

for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'insira um valor linha[{l}] coluna[{c}]: '))

#A
for l in range(0, 3):
    for c  in range (0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

#B
for l in range(0, 3):
    somaB += matriz[l][2]

#C
for c in range(0, 3):
    if matriz [1][0]:
        maiorC = matriz[1][c]
    elif matriz[1][c] > maiorC:
        maiorC = matriz[1][c]

#impressao
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()

print(f'A) a soma de todos os valores pares digitados eh {pares}')

print(f'B) a soma dos valores da terceira coluna {somaB}')

print(f'C) o maior valor da segunda linha {maiorC}')
