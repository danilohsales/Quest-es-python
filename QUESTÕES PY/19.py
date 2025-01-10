print("Mastery Learning")
print("Cálculo da nota na unidade\n")

notas = []
aprovado = False

while not aprovado:
    nota = float(input("Nota? "))
    notas.append(nota)

    if len(notas) >= 2:
        # Calcular as duas maiores notas manualmente
        maior1 = notas[0]
        maior2 = notas[1]
        
        if maior1 < maior2:
            maior1, maior2 = maior2, maior1

        for i in range(2, len(notas)):
            if notas[i] > maior1:
                maior2 = maior1
                maior1 = notas[i]
            elif notas[i] > maior2:
                maior2 = notas[i]

        media_parcial = (maior1 + maior2) / 2

        penalizacoes = (len(notas) - 2) * 0.5 if len(notas) > 2 else 0

        media_final = media_parcial - penalizacoes

        # Determinar situação
        situacao = "aprovado" if media_parcial >= 6.0 else "cursando"

        # Exibir status parcial
        print(f"Média: {media_parcial:.1f} ({situacao})")
        print(f"Penalização: {penalizacoes:.1f}")
        print()
        if situacao == "aprovado":
            aprovado = True

# Exibir resumo final
print("===")
print(f"Notas válidas: {maior1:.1f} e {maior2:.1f}")
print(f"Média parcial na unidade: {media_parcial:.1f}")
print(f"Penalizações: {penalizacoes:.1f}")
print(f"Média final na unidade: {media_final:.1f}")