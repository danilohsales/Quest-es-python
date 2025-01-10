while True:
    binario = input("")
    if binario == 'fim':
        break
    
    if len(binario) != 8:
        print("Tente novamente.")
        continue

    # Calcular parte alta (dezenas) e parte baixa (unidades)
    parte_alta = 0
    for d in range(4):
        bit = int(binario[d])
        parte_alta += bit * (2 ** (3 - d))

    parte_baixa = 0
    for u in range(4, 8):
        bit = int(binario[u])
        parte_baixa += bit * (2 ** (7 - u))

    # Verificar se as partes alta e baixa são válidas para BCD (0 a 9)
    if not (0 <= parte_alta <= 9 and 0 <= parte_baixa <= 9):
        print("BCD inválido.")
    else:
        # Formatar o resultado para ter dois dígitos
        decimal = f"{parte_alta}{parte_baixa}"  # Concatenação de parte alta e baixa
        print(decimal)  # Imprimir a saída formatada
