years = int(input())
washmachine = float(input())
toy_price = int(input())

money_from_gifts = 0
money_given = 10
toys = 0

for i in range(1, years+1):
    if i % 2 == 0:
        money_from_gifts += money_given - 1
        money_given += 10
    else:
        toys += 1

money_from_gifts += toys * toy_price

if money_from_gifts >= washmachine:
    print(F"Yes! {money_from_gifts-washmachine:.2F}")
else:
    print(F"No! {washmachine - money_from_gifts:.2F}")

