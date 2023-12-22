from datetime import date
import random

print()

def main():
    # importando a temperatura da funcao tempNuvem
    temperatura = tempNuvem()
    # importando a data da bibliotéca datetime
    today = date.today()

    vento = float(input(f'Informe a volecidade do vento (km/h): '))
    umidade = float(input(f'Informe a umidade do ar (%): '))

    print()
    if temperatura <= 0 and vento < 15 and umidade > 70:
        print(f'temperatura {temperatura}° Celsius\nA nuvem tem as condições necessárias para nevar.\
              \nHaverá neve hoje ({today}), aproveite!')
    else:
        print(f'temperatura {temperatura}° Celsius\nNão haverá neve hoje ({today})')
    print()



def tempNuvem():
    """Essa função contem uma lista com valores de temperaturas. 
    Esses valores tem que ser extraidos de forma aleatória a cada vez que o programa rodar. 
    Esse valor extraído será o valor retornado"""

    # lista com algumas temperaturas
    temperaturas = [-3,0,-5,-2,-10,-9]

    # buscando na lista um valor de forma aleatória
    
    #if random.choice(temperaturas) <= 0:
    temperatura = random.choice(temperaturas)
    
    # retornando o valor extraído da lista
    return temperatura

if __name__ == "__main__":
    main()