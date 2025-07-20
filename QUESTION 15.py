import math
# a QUESTÃO PEDE 20X20 resultado 137846528820
malha = int(input('Diga um valor para a malha'))

def caminhos_trelhica(n):
    return math.comb(2 * n, n)

print(f'{caminhos_trelhica(malha)} onde temos a malha {malha} x {malha}')
 
