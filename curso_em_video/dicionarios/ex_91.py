#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. guarde esses resultados em um dicionario. no final, coloqueesse dicionario em ordem,, sabendo que o vencedor tirou o maior numero.
import random
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': random.randint(1,6),
    'jogador2': random.randint(1,6),
    'jogador3': random.randint(1,6),
    'jogador4': random.randint(1,6),
}

for k, v in jogo.items():
    print(f"o {k} tirou {v} no dados.")
    sleep(1)
rankign = list()
rankign = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(rankign)
# for i, v in enumerate(rankign):
#     print(f'{i} lugar {v[0]} com {v[1]}')
#     sleep(1)
for i in range(len(rankign)):
    print(f'{i} lugar {rankign[i][0]} com {rankign[i][1]}')