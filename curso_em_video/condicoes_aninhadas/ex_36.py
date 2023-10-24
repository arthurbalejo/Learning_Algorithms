#escreva um programa para aprovar o emprestimo bancario para a acompra de uma casa. o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da prestacao mensal sabendo que ela nao pode exceder 30% do asalario ou entao o emprestimo sera negado

valorCasa = float(input("insira o valor da casa: "))
salario = float(input("insira o valor do salario: "))
anos = float(input("insira quantos anos ira pagar: "))

valorPrestacao = valorCasa/(anos*12)

if(valorPrestacao > salario * 0.3):
    print("emprestimo negado")
else:
    print("emprestimo deferido")