limite = int(input())

a = 0
b = 1

while a < limite:
    print(a)
    termo_a = a
    a = b
    b = termo_a + b
    
   # print(a)
   # a, b = b, a + b
