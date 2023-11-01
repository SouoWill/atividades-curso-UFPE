n1 = 0
maior_numero = 0
for c in range(0, 5):
    n1 = int(input('digite um número: '))
    if n1 > maior_numero:
        maior_numero = n1
print(f'o maior número digitado foi: {maior_numero}')