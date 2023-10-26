#verificar se o numero eh primo

numero = int(input("insira o numero: "))
soma = 0

for c in range(1, numero +1, 1):
    if(numero % c == 0):
        soma += 1

if(soma == 2):
    print("eh primo")
else:
    print("nao eh")