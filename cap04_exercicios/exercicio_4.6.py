"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km, e R$0,45
para viagens mais longas.

"""
distância = float(input("Digite a distância a percorrer: "))
if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 0.45 * distância
print(f"Preço da passagem: R$ {passagem:7.2f}")