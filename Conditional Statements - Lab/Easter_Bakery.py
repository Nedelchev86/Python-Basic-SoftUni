# 1.Цена на брашното за един килограм – реално число в интервала [0.00 … 10000.00]
# 2.Килограми на брашното – реално число в интервала [0.00 … 10000.00]
# 3.Килограми на захарта – реално число в интервала [0.00 … 10000.00]
# 4.Брой кори с яйца – цяло число в интервала [0 … 10000]
# 5.Пакети мая – цяло число в интервала [0 … 10000

flour_price = float(input())
flour_amount = float(input())
sugar_amount = float(input())
eggs_amount = int(input())
yeast = int(input())

#  цената на килограм захар е с 25% по-ниска от тази на килограм брашно
#  цената на една кора с яйца е с 10% по-висока от цената на килограм брашно
#  цената на един пакет мая е с 80% по-ниска от цената на килограм захар

sugar_price = flour_price - (flour_price * 0.25)
eggs_price = flour_price + (flour_price * 0.1)
yeast_price = sugar_price - (sugar_price * 0.8)

flour_total =(flour_price * flour_amount)
sugar_total =(sugar_price * sugar_amount)
eggs_total = (eggs_price * eggs_amount)
yeast_total = (yeast_price * yeast)
total = flour_total + sugar_total + eggs_total + yeast_total
print(F"{total:.2F}")
