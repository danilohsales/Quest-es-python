razao = int(input())

seq_inteiros = []
while True:
    entrada = input()
    if entrada == 'fim':
        break
    
    inteiros = [int(s) for s in entrada.split()]
    seq_inteiros.append(inteiros)

qntd_pa = 0
for seq in seq_inteiros:
    e_pa = True
    i = 1
    while i < len(seq):
        if seq[i] - seq[i - 1] != razao:
            e_pa = False
        i += 1
    if e_pa:
        qntd_pa += 1
    
print(qntd_pa)