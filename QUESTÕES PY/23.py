soma = 0
n_numeros = 0

while soma <= 500:
    numero = int(input())
    if numero >= 0:
        soma += numero
        n_numeros += 1
    else:
        break
if n_numeros > 0:
    media = soma / n_numeros
else:
    media = 0
    
print(soma)
print(f'{media:.2f}')
print(n_numeros)