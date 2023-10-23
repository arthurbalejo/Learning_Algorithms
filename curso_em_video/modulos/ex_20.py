# sortear a ordem de apresentacao de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

listaAlunos = []

for x in range(4):
    nome = input("digite o nome do aluno:")
    listaAlunos.append(nome)

random.shuffle(listaAlunos)

print(listaAlunos)