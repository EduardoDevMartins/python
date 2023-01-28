entrada = input('Digite a hora "exemplo: 1245 :" ')

try:
    hora = int(entrada)
    if hora == 0 or hora <= 1159:
        print('BOM DIA')
    elif hora == 1200 or hora < 1759:
        print('BOA TARDE')
    elif hora > 1800 or hora <= 2400:
        print(' BOA NOITE')

except:
    print("você digitou a hora em formato incorreto")