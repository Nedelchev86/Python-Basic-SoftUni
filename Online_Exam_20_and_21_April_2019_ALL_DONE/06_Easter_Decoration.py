
clients = int(input())
money_client = 0
count = 0
total_money = 0
for i in range(clients):
    command = input()
    while command != "Finish":
        count += 1
        if command == "basket":
            money_client += 1.50
        elif command == "wreath":
            money_client += 3.80
        else:
            money_client += 7
        command = input()
    if count % 2 == 0:
        money_client = money_client * 0.80
    total_money += money_client
    print(F"You purchased {count} items for {money_client:.2F} leva.")
    count = 0
    money_client = 0
print(F"Average bill per client is: {total_money / clients:.2F} leva.")
