def elimina_menores(num, lista):
    menores = 0
    # Itera sobre a lista de trás para frente
    indice = len(lista) - 1
    while indice >= 0:
        # Se o elemento for menor que num, remove-o da lista
        if lista[indice] < num:
            lista.pop(indice)
            menores += 1
        indice -= 1
    
    return menores

lista1 = [100, 200, 300, 400]
lista2 = [3, 5, 1, 7, 10, 9]

print(elimina_menores(4, lista2))
print(lista2)
