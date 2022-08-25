"""
Usando o else para especificar o que fazer caso o resultado da avaliação da condição
seja falso, sem precisar de um novo if.

"""
idade = int(input('Informe a idade de seu carro: '))
if idade <= 3:
    print('\033[1;36;95mCarro novo!!!\033[m')
else:
    print('\033[1;36;95mLATA VELHA!!!\033[m')
