# Livro Introdução à Programação com Pyhton de Nilo Ney
"""
Escreva um programa que converta uma temperatura digitada em Celsius ou F.
A fórmula para essa conversão é:
(9 * C / 5) + 32
"""
# Código do livro
C = float(input("Digite a temperatura em °C:"))
F = (9 * C / 5) + 32
print("%5.2f°C é igual a %5.2f°F" % (C, F))