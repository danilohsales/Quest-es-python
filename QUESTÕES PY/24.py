def busca(seq, valor):
    i = 0
    while i < len(seq):
        if seq[i] == valor:
            return i
        i += 1
    return -1

seq = [8, 9, 2, 3, 6, 10, 7, 9]
print(busca(seq, 101))