bags_price_20 = float(input())
weight = float(input())
days = int(input())
bags_number = int(input())

if weight < 10:
    bags_price_20 *= 0.2
elif weight <=20:
    bags_price_20 *= 0.5
else:
    bags_price_20 = bags_price_20
if days > 30:
    bags_price_20 *= 1.1
elif days <= 30 and days >= 7:
    bags_price_20 *= 1.15
else:
    bags_price_20 *= 1.4
print(F" The total price of bags is: {bags_number * bags_price_20:.2F} lv. ")