def tem_afinidade(l1, l2):
    artista_comun = 0
    
    for artista1 in l1:
        for artista2 in l2:
            if artista1 == artista2:
                artista_comun += 1
                
                if artista_comun >= 3:
                    return True
    return False

l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True