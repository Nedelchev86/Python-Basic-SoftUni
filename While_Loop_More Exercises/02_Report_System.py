
sum = int(input())

paymant = input()
count = 0
cash = 0
card = 0
total_card = 0
total_cash = 0
total = 0
succsess = True

while paymant != "End":
    command = int(paymant)
    count += 1
    if count % 2 == 0:
        if command < 10:
            print("Error in transaction!")
            succsess = False
        else:
            print("Product sold!")
            card += 1
            total_card += command
            total += command
    else:
        if command > 100:
            print("Error in transaction!")
            succsess = False
        else:
            print("Product sold!")
            cash += 1
            total_cash += command
            total += command
    if total >= sum:
        break

    paymant = input()

if total >= sum:
    print(F"Average CS: {total_cash / cash:.2F}")
    print(F"Average CC: {total_card / card:.2F}")
else:
    print("Failed to collect required money for charity.")