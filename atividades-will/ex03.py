pop_a = int(input('Informe a população A: '))
pop_b = int(input('Informe a população B: '))
cont = 0

taxa_crescimento_a = float(input('Informe a taxa de crescimento A: '))
taxa_crescimento_b = float(input('Informe a taxa de crescimento A: '))

while pop_a < pop_b:
    pop_a += taxa_crescimento_a * pop_a
    pop_b += taxa_crescimento_b * pop_b
    cont += 1
print(f'a população A vai demorar {cont} anos para alcançar a população B')