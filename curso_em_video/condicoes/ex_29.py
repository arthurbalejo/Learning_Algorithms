# Escreva um
# programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limita.

velocidade = float(input("insira a velocidade do carro: "))

multa = (velocidade - 80) * 7

if (velocidade > 80):
    print("tu foi multado")
    print("valor da multa: {:.2f}".format(multa))
else:
    print("tudo belezinha")
