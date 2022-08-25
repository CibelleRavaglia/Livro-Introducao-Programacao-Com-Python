"""
Estruturas aninhadas
Planos de telefone da empresa Tchau.
Abaixo de 200 minutos, a empresa cobra R$0,20 por min. Entre 200 e 400 minutos,
o preço é de R$0,18. Acima de 400 minutos, o preço por minuto é de R$0,15.

"""
minutos = int(input('Quantos minutos você utilizou este mês? '))
if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print(f'Você pagará este mês: R${minutos * preço: 6.3f}')

