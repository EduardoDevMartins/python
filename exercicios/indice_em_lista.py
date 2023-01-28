'''
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

'''


lista = []

while True:
    
    nome = input('Insira o nome na lista ou escreva (sair) para sair: ')
    lista.append(nome)
     


    if nome == 'sair':
        
        break

    for indice, nome in enumerate(lista, start=1):
        print(indice, nome)

    




