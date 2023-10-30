#crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. no final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.

lista = list()
listaC = list()
boletim = list()

while True:
    nome = str(input('insira o nome do aluno: '))
    nUm = float(input('insira a nota 1: '))
    nDois = float(input('insira a nota 2: '))
    media = (nUm + nDois) / 2
    lista.append(nome)
    lista.append(nUm)
    lista.append(nDois)
    lista.append(media)
    listaC.append(lista[:])
    lista.clear()
    decisao = str(input('deseja continuar? [S/N] '))
    if decisao in 'Nn':
        break

for elemento in listaC:
    print(f'nome: {elemento[0]:^10}', end='')
    print(f'media: {elemento[3]:^4}')

while True:
    print('*'*35)
    index = int(input('qual aluno tu quer ver as notas? [index] e 999 para sair. '))
    if index == 999:
        break
    print(listaC[index][1], listaC[index][2])
   



