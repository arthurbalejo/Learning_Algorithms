# crie um programa onde o usuario possa digitar cinco valores niumericos e cadastre-os em uma lista, ja na posicao de insercao (sem usar sort()).sortedno final, mostre a lista ordenada na tela

outroNome = []

for c in range(5):
    inserido = int(input('insira um valor: '))
    if c == 0 or inserido > outroNome[-1]:
        outroNome.append(inserido)
        print('adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(outroNome):
            if inserido <= outroNome[posicao]:
                outroNome.insert(posicao, inserido)
                print(f'adicionado na posicao {posicao} da lista')
                break
            posicao += 1

print(outroNome)