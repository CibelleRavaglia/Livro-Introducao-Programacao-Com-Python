# Livro Introdução à Programação com Pyhton de Nilo Ney
"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
pelo usuáriom assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

"""
# Código do livro
km = int(input("Digite a quantidade de quilometros percorridos:"))
dias = int(input("Digite quantos dias você ficou com o carro:"))
preço_por_dia = 60
preço_por_km = 0.15
preço_a_pagar = km * preço_por_km + dias * preço_por_dia
print("Total a pagar: R$ %7.2f" % preço_a_pagar)