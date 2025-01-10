binario = input()

decimal = 0
passos = []
for i in range(len(binario)):
    v_decimal = int(binario[i]) * (2 ** (len(binario) - i - 1))
    decimal += v_decimal
    passos.append(f'{int(binario[i])} * {2 ** (len(binario) - i - 1)} = {v_decimal}')
    
for passo in passos:
    print(passo)
print(f'{binario}(2) = {decimal}(10)')