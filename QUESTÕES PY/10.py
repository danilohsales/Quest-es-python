sequencia = input().split()

# Convertendo os elementos da sequência para inteiros
sequencia = [int(item) for item in sequencia]

# Inicializando variáveis para armazenar a maior soma e as posições da tríade com a maior soma
maior_soma = float('-inf')
indice_maior_soma = 0

# Iterando sobre a sequência para encontrar a tríade com a maior soma
for indice in range(len(sequencia) - 2):
    soma_tríade = sequencia[indice] + sequencia[indice + 1] + sequencia[indice + 2]
    if soma_tríade >= maior_soma:
        maior_soma = soma_tríade
        indice_maior_soma = indice

# Imprimindo a maior soma e as posições da tríade com a maior soma
print(f'maior soma: {maior_soma}')
print(f'tríade: posições {indice_maior_soma}, {indice_maior_soma + 1} e {indice_maior_soma + 2}')
