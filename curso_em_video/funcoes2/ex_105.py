#faça um programa que tenha uma função notas() que pode receber várias notas de alunoso e vai retornar um dicionário com as seguintes informações:
#-quantidade de notas
#-a maior nota
#-a menor nota
#-a media da turma
#-a situacao opcional()
#adicione tambem as docstrings da função

def notas(lista = [],sit=False):
    '''#faça um programa que tenha uma função notas() que pode receber várias notas de alunoso e vai retornar um dicionário com as seguintes informações:
#-quantidade de notas
#-a maior nota
#-a menor nota
#-a media da turma
#-a situacao opcional()
#adicione tambem as docstrings da função
'''
    r = dict()
    q_notas = len(lista)
    maior_notas = 0
    m_notas = 0
     
    for c in lista:
        m_notas += c
        if c > maior_notas:
            maior_notas = c
    media_notas = m_notas/len(lista)
    situacao = ''
    if media_notas > 6:
        situacao = 'RAZOAVEL'
    else:
        situacao = 'RUIM'
    if sit == False:
        dicio = {'total': str(q_notas), 
        'maior': str(maior_notas), 'media': str(media_notas)}
    else:
        dicio = {'total': str(q_notas), 
        'maior': str(maior_notas), 'media': str(media_notas),
        'situacao': situacao
        }
    return dicio

resp = notas([3.5, 10, 6.5], True)
print(resp)


    