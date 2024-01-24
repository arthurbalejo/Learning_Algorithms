#faça um programa que tenha uma função notas() que pode receber várias notas de alunoso e vai retornar um dicionário com as seguintes informações:
#-quantidade de notas
#-a maior nota
#-a menor nota
#-a media da turma
#-a situacao opcional()
#adicione tambem as docstrings da função

def notas(n = [], sit=False):
    maior  = 0
    menor = 0
    m = 0
    for c in n:
        m += c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    media = m/len(n)
    