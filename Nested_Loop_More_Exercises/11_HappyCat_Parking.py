days = int(input())
hours = int(input())
price = 0
total = 0

for d in range(1, days + 1):
    sum = 0
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            price = 2.50
        elif d % 2 != 0 and h % 2 == 0:
            price = 1.25
        else:
            price = 1
        sum += price
    total += sum
    print(F"Day: {d} - {sum:.2F} leva")
print(F"Total: {total:.2F} leva")
