salario = int(input())

if salario > 1000:
    print(round(salario * 1.10, 1))
else:
    print(round(salario * 1.15, 1))