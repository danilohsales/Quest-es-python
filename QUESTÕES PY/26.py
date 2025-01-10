def divisor(num, lista):
    posicao = 0
    for n in lista:
        if num != 0:
            if n % num == 0:
                return posicao
        posicao += 1
        
    return -1

lista1 = [100,10,40,50]
lista2 = [3,15,50,23,5]

assert divisor(10, lista1) == 0
assert divisor(5, lista2) == 1

print(divisor(23, lista2))