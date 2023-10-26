#desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final, mostre os 10 primeiros termos dessa prograssao

pTermo = int(input("insira o primeiro termo: "))
razao = int(input("insira a razao: "))
dTermo = pTermo + (10 -1 ) * razao
for c in range(pTermo, dTermo + razao, razao): #+ razao pra ele conseguir chegar no ultimo termo
    print("{}".format(c), end = " -> ")

print("terminou")


    
