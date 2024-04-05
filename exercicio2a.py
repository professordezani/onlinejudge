count = 0
razao = 0

numero = int(input())

while numero > 0:
    if count == 0:
        antecessor = numero
        count += 1
    elif count == 1:
        sucessor = numero
        count += 1
        razao = sucessor - antecessor
    else:
        antecessor = sucessor
        sucessor = numero
        if sucessor - antecessor != razao:
            print(False)
            break

    numero = int(input())
else:
    print(True)





# # Leitura dos números do terminal
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# # Verifica se a diferença entre cada par de números consecutivos é a mesma
# if b - a == c - b == d - c == e - d:
#     print(True)
# else:
#     print(False)


