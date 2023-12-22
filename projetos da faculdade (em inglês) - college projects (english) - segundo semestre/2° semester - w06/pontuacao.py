# Criar um dicionário com alguns itens
meu_dicionario = {
    "item1": 10,
    "item2": 20,
    "item3": 30,
    "item4": 40,
    "item5": 50,
    "item6": 23,
    "item7": 42
}

# Classificar o dicionário em ordem decrescente com base nos valores
dicionario_ordenado = dict(sorted(meu_dicionario.items(), key=lambda item: item[1], reverse=True))

# Inicializar uma variável para contar os itens
contador = 0

# Percorrer o dicionário ordenado
for chave, valor in dicionario_ordenado.items():
    contador += 1
    print(f"Item {contador}: {chave} - Valor: {valor}")


    
    