entrada = input()

inversa = ''
for i in range(len(entrada)- 1, -1, -1):
    inversa += entrada[i]

coincidentes = 0
for i in range(len(entrada)):
    if entrada[i] == inversa[i]:
        coincidentes += 1
        
               
print(f'A palavra {entrada} contém {coincidentes} caractere(s) coincidente(s) com a sua inversa.')