def caixa_registradora(vendas, meta):
    soma_vendas = 0
    total_comissao = 0.0
    for venda in vendas:
        soma_vendas += venda
        if venda < 1000.0:
            total_comissao += 0.05 * venda
        elif 1000.0 <= venda < 5000.0:
            total_comissao += 0.10 * venda
        else:
            total_comissao += 0.15 * venda
            
    if soma_vendas - total_comissao >= meta:
        dia = 'Lucro'
    else:
        dia = 'Prejuízo'
        
    return [soma_vendas, total_comissao, dia]

#vendas = [1000.0, 2000.0, 5000.0, 2500.0, 950.0]
assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']
#print(caixa_registradora(vendas, 2000))