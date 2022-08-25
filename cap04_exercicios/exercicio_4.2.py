"""
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km.

"""
velocidade = float(input('Qual é a sua velocidade? '))
if velocidade < 80:
    print("\033[1;31;40mTenha uma boa viagem!!!\033[m")
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"\033[1;31;40mVocê foi multado em R${multa:7.2f}!\033[m")