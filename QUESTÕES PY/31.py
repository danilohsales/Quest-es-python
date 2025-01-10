def maioridade_penal(nomes: str, idades: str) -> str:
    # Divide as strings de entrada em listas
    lista_nomes = nomes.split()  # Lista de nomes
    lista_idades = idades.split()  # Lista de idades

    # Lista para armazenar os nomes das pessoas que atingiram a maioridade penal
    maiores_de_idade = []

    # Itera sobre as listas para encontrar as pessoas maiores de idade
    for i in range(len(lista_nomes)):
        # Converte a idade para inteiro para comparação
        idade = int(lista_idades[i])

        # Se a idade for >= 18, adiciona o nome à lista
        if idade >= 18:
            maiores_de_idade.append(lista_nomes[i])

    # Retorna os nomes das pessoas maiores de idade como uma única string
    return " ".join(maiores_de_idade)

idades = ['14 21 60']
nomes = ['Jansen Italo Ana']

print(maioridade_penal('Italo', '21'))