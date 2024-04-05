n = int(input("Digite o valor de N para a série: "))

for i in range(1, n + 1):
    termo = i ** 2
    print(termo, end='')

    if i < n:
        print(', ', end='')
    else:
        print('')