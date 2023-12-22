import math

print(f"Esse sistema calcula potência total disponível pelo vento")

print()

def main():

    #   a variavel velocidade se refere a velocidade do vento em m/s
    velocidade = float(input(f'Informe a velocidade do vento em m/s: '))
    #   a variavel massa é referente a massa específica do ar em kg/m3
    massa = float(input(f'Informe a massa específica do ar em kg/m: '))
    #   A é a área de varredura das pás em rotação em m2
    area = float(input(f'Informe a área de varredura das pás em m²: '))

    # a potencia total disponivel
    w = eficiencia_turbina(area, velocidade, massa)

    print()

    print(f'A potênica total disponível pelo vento é {w:.2f} kgm²/s')
    


def eficiencia_turbina(area, velocidade, massa):
    """Essa função vai calcular a potencia total disponível pelo vento"""

    # w = a potencia total disponivel
    w = ((velocidade**3)*area*massa) / 2

    return w


main()