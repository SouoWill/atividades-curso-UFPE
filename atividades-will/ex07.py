preco = ''
total = 0
cont = 1
print('DIGITE 0 PARA PAGAR OS PRODUTOS')
while preco != 0:
    preco = float(input(f'produto {cont}: R$'))
    total += preco
    cont += 1

dinheiro = float(input('quanto você vai pagar: R$'))
troco = dinheiro - total
if troco < 0:
    print('vamos cancelar a compra, pois o valor pago nao foi o suficiente')
elif troco == 0:
    print('volte sempre')
else:
    print(f'compra realizada com sucesso\n[32mo troco é de R${troco}')