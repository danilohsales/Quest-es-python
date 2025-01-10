def encontro_vocalico(palavra):
    for i in range(len(palavra) - 1):
        if palavra[i] in 'aeiou' and palavra[i + 1] in 'aeiou':
            return True
    return False

N = int(input())

com = 0
for letra in range(N):
    palavra = input().lower()
    if encontro_vocalico(palavra):
        com += 1
        

sem = N - com

print(f'com: {com}')
print(f'sem: {sem}')
