def calcula_digitos_verificacao(cpf):
    def calcula_digito(cpf, peso):
        soma = 0
        for i in range(len(cpf)):
            soma += int(cpf[i]) * peso[i]
        resto = soma % 11
        return str(11 - resto) if resto > 1 else '0'

    peso_primeiro_digito = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    peso_segundo_digito = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    primeiro_digito = calcula_digito(cpf, peso_primeiro_digito)
    segundo_digito = calcula_digito(cpf + primeiro_digito, peso_segundo_digito)

    return primeiro_digito + segundo_digito

# Teste da função com o exemplo fornecido
assert calcula_digitos_verificacao('153245875') == '40'
