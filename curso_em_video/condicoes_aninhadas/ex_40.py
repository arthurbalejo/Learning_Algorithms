#crie um porgrama que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final, de acordo com a media atingida
#media abaico de 5.0: reprovado
#media entre 5.0 e 6.9: recuperacao
#media 7.0 ou superior: aprovado

n1 = float(input("Insira sua nota n1: "))
n2 = float(input("Insira sua nota n2: "))

media = (n1 + n2)/2

if(media < 5.0):
    print("sua media foi {} e esta reprovado".format(media))
elif(5.0 < media < 7.0):
    print("sua media foi {} e esta em recuperacao".format(media))
else:
    print("sua media foi {} e esta aprovado".format(media))