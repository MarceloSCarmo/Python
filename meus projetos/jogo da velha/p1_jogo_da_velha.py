def main():

    # Informando as posições para cada jogada
    print("Escolha uma posição para sua jogada\n\na1|a2|a3\nb1|b2|b3\nc1|c2|c3")
    print()

    dic_posicao = dicPosicao()

    # Excluindo os _ das posições inferiores do jogo da velha
    dic_posicao['c1'] = ' '
    dic_posicao['c2'] = ' '
    dic_posicao['c3'] = ' '

    # Identificando os simbolos disponíveis
    escolhaSimbolo1 = 'X'
    escolhaSimbolo2 = 'O'

    # Esse contador contará somente a estrutura de repetição whilhe, ele só pode contar até 9 porque
    # são o número de posições que ambos os jogadores conseguem escolher
    countWhile = 1
    jogo_encerrado = bool

    # Loop while continuará rodando até que o se passem 9 rodadas (limite de jogadas possíveis) ou até que haja um vencedor
    while countWhile <= 9:
        
        # Verifica se as condições para encerrar o jogo estão satisfeitas, se sim, o jogo encerra.
        status_atual = status(jogo_encerrado, dic_posicao)
        if status_atual == True:
            break
        
        # solicitando ao usuário a posição de cada jogada 
        elemento = input('informe a posição: ')
        
        # Esse contador é para ser utilizado somente dentro do For Loop
        countFor = 1
        
        # O primeiro IF verifica se os valores de cada chave estão disponíveis para serem utilizados
        # caso não estejam o programa vai executar o else e o jogador repetirá a jogada
        if dic_posicao[elemento] == ' ' or dic_posicao[elemento] == '_':
            
            # O segundo IF verifica se o elemento fornecido pelo usuário existe dentro do dicionário
            # caso não exista, a jogada é inválida
            if elemento in dic_posicao:
                
                # O terceiro IF verifica se a jogada é par ou ímpar para que cada jogador jogue na sua vez
                if countWhile % 2 == 1:
                    dic_posicao[elemento] = escolhaSimbolo1
                elif countWhile % 2 == 0:
                    dic_posicao[elemento] = escolhaSimbolo2
                
                # Esse loop verifica cada item existente no dicionário e guarda o valor atibuído
                for key, value in dic_posicao.items():
                    # Esse loop cria o formato do jogo da velha
                    #   _|_|_
                    #   _|_|_
                    #    | |
                    if countFor == 1 or countFor == 2 or countFor == 4 or countFor == 5 or countFor == 7 or countFor == 8:
                        print(value, end='|', flush=True)
                    
                    elif countFor == 3 or countFor == 6 or countFor == 9:
                        print(value)  
                    countFor += 1
        else:
            # se imprimir essa mensagem o contador tem que voltar a contagem em um número
            # dessa forma o jogador poderá repetir a jogada e escolher um dos elementos disponíveis
            print(f'Essa posição já foi escolhida. Repita a jogada.')
            countWhile -= 1

        countWhile += 1 

def dicPosicao():
    # Dicionário contendo todas as posições do jogo
    dicPosicao = {  'a1': '_',
                    'a2': '_',
                    'a3': '_',
                    'b1': '_',
                    'b2': '_',
                    'b3': '_',
                    'c1': '_',
                    'c2': '_',
                    'c3': '_',
    }

    return dicPosicao


def status(jogo_encerrado, dic_posicao):

    #condições para que X seja o vencendor
    if dic_posicao['a1'] == 'X' and dic_posicao['a2'] == 'X' and dic_posicao['a3'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['b1'] == 'X' and dic_posicao['b2'] == 'X' and dic_posicao['b3'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['c1'] == 'X' and dic_posicao['c2'] == 'X' and dic_posicao['c3'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a1'] == 'X' and dic_posicao['b1'] == 'X' and dic_posicao['c1'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a2'] == 'X' and dic_posicao['b2'] == 'X' and dic_posicao['c2'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a3'] == 'X' and dic_posicao['b3'] == 'X' and dic_posicao['c3'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a1'] == 'X' and dic_posicao['b2'] == 'X' and dic_posicao['c3'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a3'] == 'X' and dic_posicao['b2'] == 'X' and dic_posicao['c1'] == 'X':
        jogo_encerrado = True
        print(f'Jogo finalizado')

    #condições para que O seja o vencendor
    elif dic_posicao['a1'] == 'O' and dic_posicao['a2'] == 'O' and dic_posicao['a3'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['b1'] == 'O' and dic_posicao['b2'] == 'O' and dic_posicao['b3'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['c1'] == 'O' and dic_posicao['c2'] == 'O' and dic_posicao['c3'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a1'] == 'O' and dic_posicao['b1'] == 'O' and dic_posicao['c1'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a2'] == 'O' and dic_posicao['b2'] == 'O' and dic_posicao['c2'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a3'] == 'O' and dic_posicao['b3'] == 'O' and dic_posicao['c3'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a1'] == 'O' and dic_posicao['b2'] == 'O' and dic_posicao['c3'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')
    elif dic_posicao['a3'] == 'O' and dic_posicao['b2'] == 'O' and dic_posicao['c1'] == 'O':
        jogo_encerrado = True
        print(f'Jogo finalizado')

    return jogo_encerrado

if __name__=="__main__":
    main()