# um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
listaNomes = []

for x in range(4):
    nome = input("Digite o nome do aluno: ")
    listaNomes.append(nome)

sorteio = random.randrange(0, 4)

print("o sorteado foi {}".format(listaNomes[sorteio]))