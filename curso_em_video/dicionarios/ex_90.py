#faca um programa que leia nome e media de um aluno, guardando tambem a situacao em um dicionario. no final, mostre o conteudo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('insira o nome: '))
aluno['media'] = int(input('insira a media: '))
if aluno['media'] > 7:
    aluno['situacao'] = 'bom'
else:
    aluno['situacao'] = 'ruim'

for c, v in aluno.items():
    print(f'{c}: {v}')