preco_etiqueta = float(input("Digite o preço do produto: "))
opcao_pagamento = int(input("Digite a opção de pagamento (1, 2, 3 ou 4): "))

if opcao_pagamento == 1:
    preco_a_pagar = preco_etiqueta * 0.9  # Desconto de 10% para pagamento à vista em dinheiro ou cheque
elif opcao_pagamento == 2:
    preco_a_pagar = preco_etiqueta * 0.85  # Desconto de 15% para pagamento à vista no cartão de crédito
elif opcao_pagamento == 3:
    preco_a_pagar = preco_etiqueta  # Preço normal para pagamento em duas vezes sem juros
elif opcao_pagamento == 4:
    preco_a_pagar = preco_etiqueta * 1.1  # Preço com juros de 10% para pagamento em duas vezes

print("{:.1f}".format(preco_a_pagar))