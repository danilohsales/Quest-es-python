def encontra_menores(num, lista):
    for item in lista:
        if item < num:
            return item
    
    return -1

lista1 = [100,200,300,400]
lista2 = [15,12,4,9,10]

assert encontra_menores(100, lista1)
assert encontra_menores(4, lista2)

# print(encontra_menores(100, lista1))