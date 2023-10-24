# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem.cobrando R$0.50 por Km para viagens de até 200Km @ R$0.45 para viagens mais longas.
distancia = float(input("insira a distancia da viagem percorrida: "))
if(distancia < 200):
    valor = distancia * 0.50
    print("valor da viagem eh: {}".format(valor))
else:
    valor = distancia * 0.45
    print("valor da viagem eh: {}".format(valor))