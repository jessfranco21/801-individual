numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def numero():
    for p in numeros:
        if p % 2 == 0:
            print('O numero par ' + str(p) + ' é par')

    for p in numeros:
        if p % 2 != 0:
            print('O numero impar ' + str(p) + ' é par')


if numeros:
    numero()
