# Função para verificar se uma letra é uma vogal a ser substituída
def eh_vogal(letra):
    return letra.lower() in ['a', 'e', 'i', 'o']

# Função para codificar uma palavra conforme as regras fornecidas
def codificar_palavra(palavra):
    # Inicialmente, a palavra codificada é igual à primeira letra da palavra original
    palavra_codificada = palavra[0]
    # Contador para contar as substituições
    substituicoes = 0
    
    # Percorre o restante da palavra
    for i in range(1, len(palavra)):
        letra = palavra[i]
        # Verifica se a letra é uma vogal a ser substituída
        if eh_vogal(letra):
            # Substitui a vogal conforme as regras
            if letra.lower() == 'a':
                palavra_codificada += '4'
            elif letra.lower() == 'e':
                palavra_codificada += '3'
            elif letra.lower() == 'i':
                palavra_codificada += '1'
            elif letra.lower() == 'o':
                palavra_codificada += '0'
            substituicoes += 1
        else:
            palavra_codificada += letra
    
    return palavra_codificada, substituicoes

# Entrada da palavra
palavra = input().strip()

# Chama a função para codificar a palavra
palavra_codificada, substituicoes = codificar_palavra(palavra)

# Imprime a palavra codificada e a quantidade de substituições
print(f'{palavra_codificada} ({substituicoes} troca(s))')
