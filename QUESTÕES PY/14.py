peso_cont = 0
combustivel_cont = 0
altitude_cont = 0

# Variável de controle para indicar se houve dados inválidos
invalidos = False

while True:
    medicoes = input().split()

    # Verificação de dados dentro da lista de medições
    i = 0
    while i < len(medicoes):
        valor = int(medicoes[i])

        if valor < 0:
            invalidos = True
            if i == 0:
                print("Dado inconsistente. Peso negativo.")
            elif i == 1:
                print("Dado inconsistente. Combustível negativo.")
            else:
                print("Dado inconsistente. Altitude negativa.")
            break  # Para o loop interno para interromper
        
        # Se o valor é positivo ou zero, incrementa o contador apropriado
        if i == 0:
            peso_cont += 1 
        elif i == 1:
            combustivel_cont += 1
        elif i == 2:
            altitude_cont += 1 

        i += 1

    # Se houve um dado negativo, para o loop principal
    if invalidos:
        break

print(f'Peso: {peso_cont}')
print(f'Combustível: {combustivel_cont}')
print(f'Altitude: {altitude_cont}')
