"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para salários inferiores a R$1.250,00 ou iguais, calcule 15%.

salário = float(input('Informe o seu salário atual: '))
aumento1 = 0.15
aumento2 = 0.10
if salário > 1.250:
    aumento = salário * aumento2
print('Seu salário é de R${}.'.format(aumento))

#Nilo
salário = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salário > 1250:
    pc_aumento = 0.10
aumento = salário * pc_aumento
print(f"Seu aumento será de: R$ {aumento:7.2f}")

"""
salário = float(input('Informe o seu salário atual: '))
if salário > 1250:
    print('Seu aumento será de R${}.'.format(aumento2 * salário))
if salário <= 1250:
    print('Seu aumento será de R${}.'.format(aumento1 * salário))
