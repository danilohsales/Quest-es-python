def adiciona_item(item, lista):
    # Encontrar a posição correta para inserir o item
    pos = 0
    while pos < len(lista) and lista[pos] < item:
        pos += 1
    
    # Inserir o item na posição correta
    lista.append('')  # Adiciona um espaço vazio no final da lista
    for i in range(len(lista) - 1, pos, -1):
        lista[i] = lista[i - 1]
    lista[pos] = item
    
    return lista
# Exemplo de uso
lista = ['acucar', 'leite', 'paes', 'queijo']
print(adiciona_item('cafe', lista))

# Ordenação de caracteres Unicode: Cada caractere em uma string possui um valor Unicode associado. 
# Por exemplo, o valor Unicode para 'a' é 97, para 'b' é 98, e assim por diante
# 'a' < 'b' => True

# Comparação lexicográfica: Quando comparamos duas strings, o Python compara os caracteres um a um 
# na posição correspondente de cada string usando seus valores Unicode.
# A primeira diferença encontrada determina a ordem das strings.