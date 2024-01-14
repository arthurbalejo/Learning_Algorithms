#faça um programa que tenha uma função chamada area(), que receba dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    return print(f'a area eh: {a}')

#main
print('Insira a largura e o comprimento do seu terreno')
largura = int(input('largura: '))
comprimento = int(input('comprimento: '))
area(largura, comprimento)
