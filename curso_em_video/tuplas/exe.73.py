# crie uma tupla preenchida com os primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocacao. depois mostre:
# A) apenas os 5 primeiros colocados.
# B) os ultimos 4 colocados da tabela.
# C) uma lista com os teimes em ordem alfabetica.
# D) em que posicao na tabela esta o gremio

brasileirao = ('botafogo', 'bragantino', 'palmeiras', 'flamengo', 'atleticopr', 'gremio', 'atleticomg', 'fluminense', 'fortaleza', 'sao paulo', 'cuiaba', 'cruzeiro', 'corinthians', 'internacional', 'bahia', 'goias', 'vasco', 'santos','coritiba', 'americamg')

print(brasileirao[:4])
print(brasileirao[-4:])
# ou print(brasileirao[16:])
print(sorted(brasileirao))
print(brasileirao.index('gremio')+1)