soma = 0
numeros = []
while True:
    sequencia = input()
    if sequencia == 'fim':
        break
    else:
        numeros.append(sequencia)
        soma += int(sequencia)
media = soma / len(numeros)

print(f'{media:.2f}')

posicao = 1
for num in numeros:
    if num < media:
        print(f'{posicao} {num}')
    posicao += 1
