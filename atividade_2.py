telefone = input("Digite seu número de celular ")

if len(telefone) == 9 and telefone[0] == '9':
    print('Numero Válido')
else:
    print('Seu numero está invalido')