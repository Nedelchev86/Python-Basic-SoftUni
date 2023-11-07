age = int(input())
washmachine = float(input())
toy_price = int(input())
bithday_Sum = 0
total_bithday_Sum = 0
toys = 0

for i in range(1, age+1):
    if i % 2 == 0:
        bithday_Sum += 10
        total_bithday_Sum += bithday_Sum - 1
    else:
        toys += 1

grand_total = total_bithday_Sum + (toys * toy_price)

if grand_total >= washmachine:
    print(F"Yes! {grand_total-washmachine:.2F}")
else:
    print(F"No! {washmachine - grand_total:.2F}")

