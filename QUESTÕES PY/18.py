palavras = []
p_validas = []
mais_vogais = 0

while True:
    entrada = input()
    if entrada == '.':
        break
    else:
        palavras.append(entrada)
        
for palavra in palavras:
    vogais = 0
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            vogais += 1
                    
    if vogais >= len(palavra) / 2:
        mais_vogais += 1
        p_validas.append(palavra)
                
print(mais_vogais)
for p in p_validas:
    print(p)
    