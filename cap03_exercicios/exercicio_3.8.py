# Livro Introdução à Programação com Pyhton de Nilo Ney
"""
Escreva um programa que leia um valor em metros  o exiba convertido em milímetros

"""
metros = float(input("Digite o valor em metros: "))
print('O valor {}m em centimetros é {:.0f}cm'.format(metros, metros * 100))
print('O valor {}m em milimetros é {:.0f}mm'.format(metros, metros * 1000))

#Código do livro
metros = float(input("Digite o valor em metros: "))
milímetros = metros * 1000
print("%10.3f metros equivalem a %10.3f milímetros." % (metros, milímetros))