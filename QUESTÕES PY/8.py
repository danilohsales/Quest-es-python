def max_diferenca(numero_sequencia):
    for item in range(quantidade_elementos - 1):
        diferenca = abs(sequencia[item] - sequencia[item + 1])
        if diferenca > maior_diferenca:
            maior_diferenca = diferenca
            indice_maior_diferenca = item
            return True
    return False
        
quantidade_elementos = int(input())

maior_diferenca = 0
indice_maior_diferenca = 0

sequencia = []
for elemento in range(quantidade_elementos):
    numero_sequencia  = float(input())
    sequencia.append(numero_sequencia)
    
valor_anterior = sequencia[indice_maior_diferenca]
valor_atual = sequencia[indice_maior_diferenca + 1]

print(f'{valor_anterior} e {valor_atual}')
        