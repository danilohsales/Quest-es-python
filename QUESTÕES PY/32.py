def multiplica_lista(n,lista):
    resultado = []
    for _ in range(n):
        for item in lista:
            resultado.append(item)       
    return resultado

nomes = ['joao', 'pedro']

#n = int(input())
#nomes = input().split()

#lista_multi = multiplica_lista(n,nomes)
#print(lista_multi)
#print(multiplica_lista(2,nomes))



# O que a função faz, em resumo, é criar uma lista resultante contendo
# N vezes a sequência dos elementos de LISTA.

# Isso é obtido através da combinação de dois loops FOR
# que geram a multiplicação desejada. '''