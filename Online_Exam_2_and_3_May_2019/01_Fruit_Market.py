# 1. Цена на ягодите в лева – реално число в интервала [0.00 … 10000.00]
# 2. Количество на бананите в килограми – реално число в интервала [0.00 … 1 0000.00]
# 3. Количество на портокалите в килограми – реално число в интервала [0.00 … 10000.00]
# 4. Количество на малините в килограми – реално число в интервала [0.00 … 10000.00]
# 5. Количество на ягодите в килограми – реално число в интервала [0.00 … 10000.00

price_strawberries= float(input())
price_raspberries = price_strawberries / 2
price_oranges =  price_raspberries * 0.60
price_bananas = price_raspberries * 0.2

quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

total = (price_oranges * quantity_oranges) + (price_bananas * quantity_bananas ) + \
(price_raspberries * quantity_raspberries) + (price_strawberries * quantity_strawberries)

print(F"{total:.2F}")
