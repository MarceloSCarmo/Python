from datetime import date


def main():
    
    dicionario = dicItensDisponiveis()

    valorCompras = itensSelecionados(dicionario)

    print(valorCompras)

def dicItensDisponiveis():

    dicCompras:{"maçã": 5.50,
              "peito de frango": 18.90,
              "kitkat": 4.50,
              "arroz": 6.20,
              "banana": 3.15,
              "manteiga": 26,
              "macarrão": 4.95
    }

    return dicCompras

def itensSelecionados(dicCompras):

    INDEX_1 = dicCompras['maçã']
    INDEX_2 = dicCompras['peito de frango']
    INDEX_3 = dicCompras['kitkat']
    INDEX_4 = dicCompras['arroz']
    INDEX_5 = dicCompras['banana']
    INDEX_6 = dicCompras['manteiga']
    INDEX_7 = dicCompras['macarrão']

    # somando as compras.
    soma = INDEX_1 + INDEX_2 + INDEX_3 + INDEX_4 + INDEX_5 + INDEX_6 + INDEX_7

    return soma

if __name__=="__main__":
    main()