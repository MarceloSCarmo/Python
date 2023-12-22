import math

def main():

    # chamando o dicPolinomio por meio de sua função
    # e guardando as informações na variável dicionário
    dicionario = dicionarioVariaveis()

    funcao = funcaoSegundoGrau(5, dicionario)
    delta = encontrandoDelta(dicionario)

    print(f'valor da função: {funcao:.0f}\n')
    print(f'valor do delta é: {delta:.0f}\n')



def dicionarioVariaveis():
    """Essa função contém o dicionário que possui os
       valores das constantes da função de 2° grau.
    """

    # criando o dicionário
    dicPolinomio = {
                   "a": 6,
                   "b": -4,
                   "c": 3
    }
    
    # retornando o dicionário
    return dicPolinomio


def funcaoSegundoGrau(x, dicPolinomio):
    """Essa função extrai os valores das constantes de dentro do dicionário
       que é fornecido por meio do parâmetro dicPolinomio.
       A função polinomio recebe a formula da função de 2°, o qual utilizará
       o valor da variável x para informar o ponto de inflexão.
    """

    # encontrando os valores de cada constante
    a = dicPolinomio['a']
    b = dicPolinomio['b']
    c = dicPolinomio['c']

    polinomio = float(a)*(x**2) - float(b)*x + float(c)
    
    # retornando o valor da função dado a variável x
    return polinomio

def encontrandoDelta(dicPolinomio):
    """Essa função extrai os valores das constantes de dentro do dicionário
       que é fornecido por meio do parâmetro dicPolinomio.
       Com isso a função encontrará a constante delta
    """

    a = dicPolinomio['a']
    b = dicPolinomio['b']
    c = dicPolinomio['c']

    # formula para encontrar o delta
    delta = (float(b)**2) - 4*(float(a)*float(c))

    # retorna o valor do delta
    return delta



if __name__=='__main__':
    main()