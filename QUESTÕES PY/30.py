def inverte_subseq(seq, ini, count):
    
    copia = []
    for i in range(count):
        copia.append(seq[ini + i])
    
    for i in range(count // 2):
        primeiro = ini + i
        ultimo = ini + count - 1 - i
        
        seq[primeiro], seq[ultimo] = seq[ultimo], seq[primeiro]
        
        
    return copia

# nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
# assert inverte_subseq(nums1, 1, 3) == [2, 3, 4]
# assert nums1 == [1, 4, 3, 2, 5, 6, 7, 8]

    # Teste 2: Invertendo 2 elementos a partir do índice 3
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# assert inverte_subseq(nums, 3, 2) == [4, 5]
# assert nums == [1, 2, 3, 5, 4, 6, 7, 8]


# print(inverte_subseq(nums1, 1, 3))