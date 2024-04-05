primeiro_termo = int(input("Digite o primeiro termo da série: "))
segundo_termo = int(input("Digite o segundo termo da série: "))
n = int(input("Digite o número de termos da série que deseja imprimir: "))

serie_fetuccine = f'{primeiro_termo} {segundo_termo}'
    
for i in range(2, n):
    # Se o índice é par, soma os dois últimos termos
    if i % 2 == 0:  
        novo = segundo_termo + primeiro_termo
    # Se o índice é ímpar, subtrai os dois últimos termos
    else:  
        novo = segundo_termo - primeiro_termo
    
    primeiro_termo, segundo_termo = segundo_termo, novo
    serie_fetuccine += f' {novo}'

print(serie_fetuccine)
