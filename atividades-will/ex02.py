pop_a = 80000
pop_b = 200000
cont = 0

taxa_crescimento_a = 0.03
taxa_crescimento_b = 0.015
while pop_a < pop_b:
    pop_a += taxa_crescimento_a * pop_a
    pop_b += taxa_crescimento_b * pop_b
    cont += 1
print(f'a população A vai demorar {cont} anos para alcançar a população B')