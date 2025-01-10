def soma_intervalo(a, b):
    soma = 0
    
    for i in range(a, b + 1):
        soma += i
    return soma

print(soma_intervalo(5, 10))