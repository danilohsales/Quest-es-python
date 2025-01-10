def is_substring(str1, str2):
    # Caso especial: Se str2 for uma string vazia, sempre será uma substring.
    if not str2:
        return True
    
    # Comprimentos das strings
    len1 = len(str1)
    len2 = len(str2)
    
    # Se a string menor for maior do que a maior, não pode ser uma substring
    if len2 > len1:
        return False
    
    # Loop para verificar se str2 é uma substring de str1
    for i in range(len1 - len2 + 1):
        # Se a substring de str1 a partir do índice i até i+len2 for igual a str2, retornamos True
        if str1[i:i + len2] == str2:
            return True
    
    # Se não encontramos nenhuma correspondência, retornamos False
    return False
# Testes
assert is_substring('boiada', 'oi')  # Deve ser True, pois 'oi' é substring de 'boiada'
assert not is_substring('casorio', 'casa')  # Deve ser False, pois 'casa' não é substring de 'casorio'

print(is_substring('boiada', 'oi'))
print("Todos os testes passaram!")
