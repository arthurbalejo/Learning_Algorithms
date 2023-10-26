#crie um programa que elia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores
somaA = 0
somaN = 0
for c in range(7):
    ano = int(input("insira a data de nascimento:"))
    idade = 2023 - ano
    if(idade > 21):
        somaN += 1
    else:
        somaA += 1

print("tem {} pessoas que atingiram a maioridade".format(somaA))
print("tem {} pessoas que nao atingiram a maioridade".format(somaN))