#faca um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou.
#o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gols=0):
    print(f'o jogador {jogador} fez {gols} no campeonato.')

j = str(input('insira o nome do jogador: '))
g = str(input('insira o numero de gols: '))

ficha(j, g)

