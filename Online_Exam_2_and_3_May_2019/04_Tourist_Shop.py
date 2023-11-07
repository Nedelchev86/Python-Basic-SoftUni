# От конзолата се чете:
#  На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
#  След това поредица от два реда (до получаване на команда "Stop" или при заявка за купуване на
# продукт, чиято стойност е по-висока от наличния бюджет) :
# o Име на продукта – текст
# o Цена на продукта – реално число в интервала [1.00… 5000.00

budget = float(input())
total = 0
count = 0

while budget >= total:
    product_name = input()
    if product_name == "Stop":
        print(F"You bought {count} products for {total:.2F} leva.")
        break
    count += 1
    price = float(input())
    if count % 3 == 0:
        price = price / 2
    total += price

else:
    print("You don't have enough money!")
    print(F"You need {total - budget:.2F} leva!")