#simulador de poupanca--
aporte = float(input("quanto voce vai depositar por mes?"))
juros = float ("qual e a taxa de juros atual da poupanca? "))
meses = int(input("por quantos meses voce vai investir"))
juros_decimal = juros/100
total = 0 
for mes in range(1,meses + 1):
    total = total + aporte
    total = total + (total*juros_decimal)
    print(f"mes{mes}: saldo total R$ {total}"
    print(f"ao final de {meses}meses,voce tera o valor de R$:{total}:2f}")