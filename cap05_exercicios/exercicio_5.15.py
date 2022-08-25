"""
Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
Utiliza a tabela de códigos da página 92.
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro "Código inválido"

"""
#Minha solução
"""
código = int(input('Informe o código do produto (1, 2, 3, 5 ou 9): '))
quantidade = int(input('Informe a quantidade do produto: '))
if código == 1:
    preço = 0.50
else:
    print('Código inválido!!!')
if código == 2:
    preço = 1.00
else:
    print('Código inválido!!!')
if código == 3:
    preço = 4.00
else:
    print('Código inválido!!!')
if código == 5:
    preço = 7.00
else:
    print('Código inválido!!!')
if código == 9:
    preço = 8.00
else:
    print('Código inválido!!!')
"""
apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair): "))
    preço = 0
    if código == 0:
        break
    elif código == 1:
        preço = 0.50
    elif código == 2:
        preço = 1.00
    elif código == 3:
        preço = 4.00
    elif código == 5:
        preço = 7.00
    elif código == 9:
        preço = 8.00
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preço * quantidade)
print(f"Total a pagar R${apagar:8.2f}")
