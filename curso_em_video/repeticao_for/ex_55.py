# faca um programa que leia o peso de cinco pessoas. no final mostre qual foi o m,aior e o menor peso lidos.
maiorPeso = 0
menorPeso = 0
for c in range(6):
    peso = float(input("insira o peso: "))
    if(c == 0):
        maiorPeso = peso
        menorPeso = peso
    else:
        if(peso > maiorPeso):
            maiorPeso = peso
        if(peso < menorPeso):
            menorPeso = peso

print("maior peso eh {}, e o menos eh {}".format(maiorPeso, menorPeso))