while True:
    # Lê a sequência do usuário
    sequencia = input().strip()  # remove espaços em branco
    
    # Obter o último bit (bit de paridade)
    bit_paridade = sequencia[len(sequencia) - 1]
    
    # Inicializa o contador para os bits '1'
    binario_1 = 0
    
    # Conta os bits '1' da parte principal da sequência (excluindo o bit de paridade)
    for i in range(len(sequencia) - 1):
        if sequencia[i] == '1':
            binario_1 += 1
    
    # Determina a paridade esperada
    paridade = ''
    
    if binario_1 % 2 == 1:
        paridade = '1'
    else:
        paridade = '0'
    
    # Verifica se o bit de paridade corresponde ao esperado
    if bit_paridade != paridade:
        # Se não corresponder, imprima o erro e saia do loop
        print(f"ERRO: {sequencia}")
        break
