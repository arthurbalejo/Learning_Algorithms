#faca um programa que ajude um jogador da mega sena a criar opalpites. o programa vai perguntar quantaos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random

nJogos = int(input('Quantos jogos serao gerados? '))

preJogos = []
jogo = []

contadorJ = 0

while nJogos > contadorJ:
    contador = 0
    while True:
        numero = random.randint(0,60)
        if numero not in preJogos:
            preJogos.append(numero)
            contador += 1
        if contador >= 6:
            break
    jogo.append(preJogos[:])
    preJogos.clear()
    contadorJ += 1
       
for i in range(0, nJogos):
    print(f'jogo {i+1} = {jogo[i]}')

#minha solucao nao consegue verificar maisa de uma vez
# for i in range(0, nJogos):
#     for c in range(0, 7):
#         numero = random.randint(0,60)
#         if numero not in preJogos:
#             preJogos.append(numero)
#         else:
#             numero = random.randint(0,60)
#     jogo.append(preJogos[:])
#     preJogos.clear()

for i in range(0, nJogos):
    print(f'jogo {i+1} = {jogo[i]}')