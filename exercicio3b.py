total = 0
while True:
    idade = int(input("Idade do membro da família: "))
    if idade < 0:
        break
    if idade <= 10:
        valor_mensal = 30
    elif 10 < idade <= 29:
        valor_mensal = 60
    elif 29 < idade <= 45:
        valor_mensal = 120
    elif 45 < idade <= 59:
        valor_mensal = 150
    elif 59 < idade <= 65:
        valor_mensal = 250
    else:
        valor_mensal = 400
        
    total += valor_mensal

print(round(float(total), 1))
