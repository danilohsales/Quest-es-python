media_ssp = float(input())

soma = 0
sequencia_validas = ''

while True:
    sequencia = input()
    if sequencia == 'fim':
        break
    
    s_inteiros = [int(parte) for parte in sequencia.split()]
    soma = 0
    for valor in s_inteiros:
        soma += valor
        
    if len(s_inteiros) == 0:
        continue
    media = soma / len(s_inteiros)
    
    if media < media_ssp / 2:
        break
    if media > media_ssp:
        if sequencia_validas:
            sequencia_validas += ','
        sequencia_validas += sequencia
        print(sequencia_validas)