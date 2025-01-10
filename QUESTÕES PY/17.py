razao = float(input())

peso_limite = 700
peso_atual = 0
total_pessoas = 0
crianca = 0
adulto = 0

elevador = []

while True:
    pessoas = input()
    pessoa, peso = pessoas.split()
    peso = float(peso)
    
    if peso_atual + peso > peso_limite:
        break
    
    if pessoa == 'c':
        if adulto == 0 or (crianca + 1) / adulto > razao:
            break
        crianca += 1
    elif pessoa == 'a':
        adulto += 1
        
    elevador.append((pessoa, peso))
    total_pessoas += 1
    peso_atual = peso_atual + peso
    
print('Limite atingido.')
print(f'Elevador saiu com {total_pessoas} pessoas e {peso_atual:.2f} kg.')