#faca um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra a:
#em que posicao ela aparece pela primeira vez
#em que posicao ela aparece pela ultima vez
frase = str(input("insira sua frase:")).strip().lower()

print("letra A aparece {} vezes" .format(frase.count("a")))

print("primeira letra a se encontra na posicao:  {}" .format(frase.find("a") + 1))

print("ultima letra a se encontra na posicao:  {}" .format(frase.rfind("a") + 1))