# 1.Цена на брашното за един килограм – реално число в интервала [0.00 … 10000.00]
# 2.Килограми на брашното – реално число в интервала [0.00 … 10000.00]
# 3.Килограми на захарта – реално число в интервала [0.00 … 10000.00]
# 4.Брой кори с яйца – цяло число в интервала [0 … 10000]
# 5.Пакети мая – цяло число в интервала [0 … 10000]

price_flour = float(input())
flour = float(input())
sugar = float(input())
eggs = int(input())
yeast = int(input())


price_sugar = 0.75 * price_flour
price_eggs = 1.1 * price_flour
price_yeast = 0.2 * price_sugar

total = price_flour * flour + price_yeast * yeast + price_eggs * eggs + price_sugar * sugar
print(F"{total:.2F}")