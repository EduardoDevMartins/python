frase = 'O Python é uma linguagem de programação '\
    'multiparadigma.' \
    'Python foi criado por Guido van Ropssum.'

i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < qtd_atual:
        apareceu_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1

print(
    f'A letra que apareceu mais vezes foi: "{letra_que_apareceu_mais_vezes}".')
print(f'Que apareceu {apareceu_mais_vezes} x')
