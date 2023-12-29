# Informando as posições para cada jogada
print("Escolha uma posição para sua jogada\n\na1|a2|a3\nb1|b2|b3\nc1|c2|c3")
print()

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
# Excluindo os _ das posições inferiores do jogo da velha
dicPosicao['c1'] = ' '
dicPosicao['c2'] = ' '
dicPosicao['c3'] = ' '


# Identificando os simbolos disponíveis
escolhaSimbolo1 = 'X'
escolhaSimbolo2 = 'O'

# Esse contador contará somente a estrutura de repetição whilhe, ele só pode contar até 9 porque
# são o número de posições que ambos os jogadores conseguem escolher
countWhile = 1

# Loop while continuará rodando até que o se passem 9 rodadas (limite de jogadas possíveis) ou até que haja um vencedor
while countWhile <= 9:
    
    #condições para que X seja o vencendor
    if dicPosicao['a1'] == escolhaSimbolo1 and dicPosicao['a2'] == escolhaSimbolo1 and dicPosicao['a3'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['b1'] == escolhaSimbolo1 and dicPosicao['b2'] == escolhaSimbolo1 and dicPosicao['b3'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['c1'] == escolhaSimbolo1 and dicPosicao['c2'] == escolhaSimbolo1 and dicPosicao['c3'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a1'] == escolhaSimbolo1 and dicPosicao['b1'] == escolhaSimbolo1 and dicPosicao['c1'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a2'] == escolhaSimbolo1 and dicPosicao['b2'] == escolhaSimbolo1 and dicPosicao['c3'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a3'] == escolhaSimbolo1 and dicPosicao['b3'] == escolhaSimbolo1 and dicPosicao['c3'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a1'] == escolhaSimbolo1 and dicPosicao['b2'] == escolhaSimbolo1 and dicPosicao['c3'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a3'] == escolhaSimbolo1 and dicPosicao['b2'] == escolhaSimbolo1 and dicPosicao['c1'] == escolhaSimbolo1:
        print(f'Jogo finalizado')
        break

    #condições para que O seja o vencendor
    elif dicPosicao['a1'] == escolhaSimbolo2 and dicPosicao['a2'] == escolhaSimbolo2 and dicPosicao['a3'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['b1'] == escolhaSimbolo2 and dicPosicao['b2'] == escolhaSimbolo2 and dicPosicao['b3'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['c1'] == escolhaSimbolo2 and dicPosicao['c2'] == escolhaSimbolo2 and dicPosicao['c3'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a1'] == escolhaSimbolo2 and dicPosicao['b1'] == escolhaSimbolo2 and dicPosicao['c1'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a2'] == escolhaSimbolo2 and dicPosicao['b2'] == escolhaSimbolo2 and dicPosicao['c3'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a3'] == escolhaSimbolo2 and dicPosicao['b3'] == escolhaSimbolo2 and dicPosicao['c3'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a1'] == escolhaSimbolo2 and dicPosicao['b2'] == escolhaSimbolo2 and dicPosicao['c3'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    elif dicPosicao['a3'] == escolhaSimbolo2 and dicPosicao['b2'] == escolhaSimbolo2 and dicPosicao['c1'] == escolhaSimbolo2:
        print(f'Jogo finalizado')
        break
    else:
        
        # solicitando ao usuário a posição de cada jogada 
        elemento = input('informe a posição: ')
        
        # Esse contador é para ser utilizado somente dentro do For Loop
        countFor = 1
        
        # O primeiro IF verifica se os valores de cada chave estão disponíveis para serem utilizados
        # caso não estejam o programa vai executar o else e o jogador repetirá a jogada
        if dicPosicao[elemento] == ' ' or dicPosicao[elemento] == '_':
            
            # O segundo IF verifica se o elemento fornecido pelo usuário existe dentro do dicionário
            # caso não exista, a jogada é inválida
            if elemento in dicPosicao:
                
                # O terceiro IF verifica se a jogada é par ou ímpar para que cada jogador jogue na sua vez
                if countWhile % 2 == 1:
                    dicPosicao[elemento] = escolhaSimbolo1
                elif countWhile % 2 == 0:
                    dicPosicao[elemento] = escolhaSimbolo2
                
                # Esse loop verifica cada item existente no dicionário e guarda o valor atibuído
                for key, value in dicPosicao.items():
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