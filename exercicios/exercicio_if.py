primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite outro valor: ')
valor1 = int(primeiro_valor)
valor2 = int(segundo_valor)

texto1 = f'o primeiro valor {valor1:.2f} é maior que o segundo valor: {valor2:.2f}'
texto2 = f'o primeiro valor {valor2:.2f} é maior que o segundo valor: {valor1:.2f}'

if valor1 > valor2:
    print(texto1)

elif valor2 > valor1:
    print(texto2)

elif valor1 == valor2:
    print('Os valores são iguais')
