"""
Escreva um programa que leia os números inteiros no teclado.
O programa deve ler os números até que o usuário digite 0. No final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.

"""
soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f"Média: {soma/quantidade:10.2f}")