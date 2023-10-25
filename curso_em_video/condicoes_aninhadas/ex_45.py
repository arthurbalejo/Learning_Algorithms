#pedra papel e teseoura

import random
itens = ('PEDRA', 'PAPEL', 'TESOURA')
acaoPc = random.randint(0, 2) #zero a dois

acaoJ = int(input('''SUAS ACOES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual eh a sua jogada? '''))

print("JO")
print("KEN")
print("PO")

print("-" * 22)
print("computador jogou {}".format(itens[acaoPc]))
print("jogador jogou {}".format(itens[acaoJ]))
print("-" * 22)

if(acaoPc == 0):
    if(acaoJ == 0):
        print("empate")
    elif(acaoJ == 1):
        print("venceu")
    else:
        print("perdeu")
elif(acaoPc == 1):
    if(acaoJ == 0):
        print("perdeu")
    elif(acaoJ == 1):
        print("empate")
    else:
        print("venceu")
elif(acaoPc == 2):
    if(acaoJ == 0):
        print("venceu")
    elif(acaoJ == 1):
        print("perdeu")
    else:
        print("empate")
