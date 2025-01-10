from math import sqrt
sequencia1 = input().split()
sequencia2 = input().split()

soma1 = 0
sequencia_num1 = []
for i in range(len(sequencia1)):
    s1 = float(sequencia1[i])
    sequencia_num1.append(s1)
    soma1 += s1
media1 = soma1 / (len(sequencia1))

soma2 = 0
sequencia_num2 = []
for i in range(len(sequencia2)):
    s2 = float(sequencia2[i])
    sequencia_num2.append(s2)
    soma2 += s2
media2 = soma2 / (len(sequencia2))

soma_quadrados1 = 0
for valor in range(len(sequencia_num1)):
    diferença = (sequencia_num1[valor] - media1) ** 2
    soma_quadrados1 += diferença
    divide_n1 = soma_quadrados1 / (len(sequencia1) - 1)
    desvio = sqrt(divide_n1)

soma_quadrados2 = 0
for valor1 in range(len(sequencia_num2)):
    diferença1 = (sequencia_num2[valor1] - media2) ** 2
    soma_quadrados2 += diferença1
    divide_n2 = soma_quadrados2 / (len(sequencia2) - 1)
    desvio1 = sqrt(divide_n2)

if desvio1 > desvio:
    print(f'A sequencia 2 possui o maior desvio padrão ({desvio1:.2f})')
elif desvio > desvio1:
    print(f'A sequencia 1 possui o maior desvio padrão ({desvio:.2f})')
else:
    print(f'As sequências possuem o mesmo desvio padrão ({desvio:.2f})')