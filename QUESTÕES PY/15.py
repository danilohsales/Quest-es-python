# Leitura da posição inicial
entrada = input()
linha, coluna = entrada.split()
pos_linha = int(linha)
pos_coluna = int(coluna)

# Loop para processar os comandos de movimentação
while True:
    cursor = input().strip()
    if cursor == '':  # Linha vazia indica o fim da entrada
        break
    
    movimento = cursor.split()
    distancia = int(movimento[0])
    direcao = movimento[1]
    
    if direcao == 'h':  # Mover coluna para a esquerda: - coluna
        pos_coluna -= distancia
    elif direcao == 'j':  # Mover linha para baixo: + linha
        pos_linha += distancia
    elif direcao == 'l':  # Mover coluna para a direita: + coluna
        pos_coluna += distancia
    elif direcao == 'k':  # Mover linha para cima: - linha
        pos_linha -= distancia
    
    # Impressão da posição atual do cursor
    print(f'[{pos_linha} {pos_coluna}]')
