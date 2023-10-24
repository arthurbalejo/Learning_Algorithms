import random

ni = random.randrange(0,5)

ad = int(input("Adivinhe o numero escolhido: "))

if (ad == ni):
    print("acertou")
else:
    print("errou")