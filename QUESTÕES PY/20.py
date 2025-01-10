m = int(input())
n = int(input())

if m > n:
    maior = m
    menor = n
else:
    maior = n
    menor = m
    
while menor != 0:
    resto = maior % menor
    maior = menor
    menor = resto
    
mdc = maior
print(mdc)