import random

ni = random.randrange(0,10)

ad = int(input("Adivinhe o numero escolhido: "))

tentativas = 1

# if (ad == ni):
#     print("acertou")
# else:
#     print("errou")

while ad != ni:
    tentativas += 1
    ad = int(input("Adivinhe o numero escolhido: "))

print("numero de tentativas foi {}".format(tentativas))
print(ni)