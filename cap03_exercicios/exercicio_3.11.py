# Livro Introdução à Programação com Pyhton de Nilo Ney
"""
Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar

"""
"""
preco_inicial = float(input("Informe o preço da mercadoria: "))
p_desconto = float(input("Informe o percentual de desconto: "))
preco_final = preco_inicial * p_desconto /100
print(" O preço a pagar é" % (preco_final)
"""

#Código do livro
preço = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
valor_do_desconto = preço * desconto / 100
a_pagar = preço - valor_do_desconto
print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preço))
print("vale R$ %7.2f." % valor_do_desconto)
print("O valor a pagar é de R$ %7.2f" % a_pagar)

