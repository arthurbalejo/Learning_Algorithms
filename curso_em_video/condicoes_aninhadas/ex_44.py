#elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
#a vista dinheiro/cheue: 10% de desconto
#a vista no cartao: 5% de desconto
#em ate 2x no cartao: preco normal
#3x ou mais no carta: 20% de juros
#''' pode usar varias linhas
n = int(input('''FORMAS DE PAGAMENTO
[1] a vista
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao'''))

pnormal = float(input("insira o preco normal do produto: "))

if (n == 1):
    preco = pnormal * 0.9
    print("preco final do produto e: {}".format(preco))
elif(n == 2):
    preco = pnormal * 0.95
    print("preco final do produto e: {}".format(preco))
elif(n == 3):
    preco = pnormal
    print("preco final do produto e: {}".format(preco))
elif(n == 4):
    preco = pnormal * 1.20
    print("preco final do produto e: {}".format(preco))
else:
    print("valor invalido")

