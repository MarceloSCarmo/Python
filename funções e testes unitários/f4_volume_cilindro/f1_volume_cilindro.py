import math

def main():

    raio_circunferencia = float(input('Qual o tamanho do raio do cilindro (em cm)? '))
    altura = float(input('Qual a altura do cilindro (em cm)? '))
    
    volume = volume_cilindro(raio_circunferencia, altura)

    print(f'O volume é: {volume:.2f} cm³')

def volume_cilindro(raio, altura):
    """Essa função calcula o volume total do cilindro"""

    # calcula o volume total do objeto
    volume_total = math.pi * (raio**2) * altura

    return volume_total

main()