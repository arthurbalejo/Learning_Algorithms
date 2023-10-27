# crie um programa que tenha uma tupla unica com nomes de profutos e seus respectivos precos, na sequencia. no final, mostre uma listagem de precos, organizando os dados em forma tabular

listagem = ('lapis', 1.75,
'borracha', 2,
'caderno', 15.90,
'estojo', 25,
'tranferido', 4.20,
'compasso', 9.99,
'mochila', 120.32,
'canetas', 22.30,
'livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-'*40)
for c in range(0,len(listagem),2):
    print(f'{listagem[c]:.<30} R$ {listagem[c + 1]:>5.2f}')
print('-'*40)