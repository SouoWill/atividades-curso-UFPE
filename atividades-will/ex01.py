nota = float(input('Digite um Número de 0 a 10: '))

while nota < 0 or nota > 10:
    print('Digite uma nota válida.')
    nota = float(input('Digite um Número de 0 a 10: '))

print('Parabens sua nota é: ', nota)

