def ajusta_prioridades(fila):
    # Listas para armazenar prioritários e não prioritários
    prioritarios = []
    nao_prioritarios = []
    
    # Separar os códigos em prioritários e não prioritários
    for codigo in fila:
        if codigo % 10 < 6:
            prioritarios.append(codigo)
        else:
            nao_prioritarios.append(codigo)
    
    # Reconstituir a fila original
    i = 0
    for codigo in prioritarios:
        fila[i] = codigo
        i += 1
    for codigo in nao_prioritarios:
        fila[i] = codigo
        i += 1

# Teste dos exemplos fornecidos
fila = [327, 228, 516, 535, 248, 532]
ajusta_prioridades(fila)
print(fila)  # Output esperado: [535, 532, 327, 228, 516, 248]

fila = [219, 638, 263, 621, 482, 616]
ajusta_prioridades(fila)
print(fila)  # Output esperado: [263, 621, 482, 219, 638, 616]
