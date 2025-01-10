def gera_emails(nomes):
    emails = []
    for nome in nomes:
        partes = nome.split()
        p_nome = partes[0].lower()
        u_nome = partes[-1].lower()
        nome_final = p_nome + '.' + u_nome + '@ccc.ufcg.edu.br'
        emails.append(nome_final)
        
    return emails

nomes = ['Mariana Silva Lima', 'Joao Arthur', 'Pedro Alvares Cabral']
print(gera_emails(nomes))