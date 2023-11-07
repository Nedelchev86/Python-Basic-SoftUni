#  Бюджет – реално число в интервала [0.00… 10000.00]
#  Колко литра гориво ще са им нужни – реално число в интервала [1.00… 50.00]
#  Ден от седмицата – текст с възможности "Saturday" и "Sunday"

budget = float(input())
quantity_diesel = float(input())
day = input()

price_for_diesel = 2.1
guide =  100

# В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%

total_for_diesel = quantity_diesel * price_for_diesel
grand_total = total_for_diesel + guide

if day == "Saturday":
    grand_total = grand_total * 0.90
else:
    grand_total = grand_total * 0.80

if budget >= grand_total:
    print(F"Safari time! Money left: {budget - grand_total:.2F} lv.")
else:
    print(F"Not enough money! Money needed: {grand_total - budget:.2F} lv.")