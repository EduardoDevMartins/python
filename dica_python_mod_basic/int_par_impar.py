'''
Programa para aceitar apenas numeros inteiros, e informar
se ele é par ou impar;

'''


numero_int = input('Digite um número: ')

try:
    numero_int = float(numero_int)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero {numero_int} é {par_impar_texto}')

except:
    print('você não digitou um número inteiro')