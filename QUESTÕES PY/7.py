n_palavras = int(input())
 

lista = []
for _ in range(n_palavras):
    palavras = input()
    lista.append(palavras)
    
vogais = 'aeiouAEIOU'
com = 0
sem = 0
for palavra in lista: 
    for i in range(len(palavra) - 1):
        if palavra[i] in vogais and palavra[i + 1] in vogais:
            com += 1
            break
    else:
        sem += 1

print(com)
print(sem)
