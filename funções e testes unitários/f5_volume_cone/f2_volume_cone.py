import math

def main():

    # Solicitar os valores de raio e altura do cone para o usuário
    raio = float(input(f"Informe o valor do raio em cm²: "))
    altura = float(input(f"Informe a altura em cm²: "))

    # importando a função volume_cone que contém a formula do volume do cone 
    volume = volume_cone(raio, altura)

    # imprimindo o volume do cone
    print(f"O volume do cone é: {volume:.2f} cm³.")

def volume_cone(raio, altura):
    """Essa função calcula o volume do cone"""

    # formula para calcular o volume do cone

    volume_total = (math.pi * (raio**2) * altura) / 3

    return volume_total

main()