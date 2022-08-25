"""
Escreva um programa para aprovar o empréstimo bancário para comprar uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e quantidade de ano
a pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número
de meses a pagar.

#Minha solução
valor_casa = float(input('Qual é o valor do imóvel que você deseja comprar? R$'))
salário = float(input('Qual é o valor do seu salário? R$'))
anos_pagamento = int(input('Em quantos anos você pretende pagar? '))
meses = anos_pagamento * 12
prestação = valor_casa / meses
if meses > salário * 0.3:
    print('Infelizmente, você não é elegível para esse empréstimo!')
else:
    print('Parabéns, arromabado. O valor da prestação é de {}.'.format(prestação))

"""
#Solução Nilo
valor = float(input("Digite o valor da casa: "))
salário = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))
meses = anos * 12
prestacao = valor / meses
if prestacao > salário * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")

