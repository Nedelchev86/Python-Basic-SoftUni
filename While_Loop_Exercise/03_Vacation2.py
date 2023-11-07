needen_money = float(input())
owned_money = float(input())
days_Counter = 0
spending_counter = 0

while owned_money < needen_money and spending_counter <5:
    command = input()
    money = float(input())
    days_Counter += 1
    if command == "save":
        owned_money += money
        spending_counter = 0
    elif command == "spend":
        owned_money -= money
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0
    if spending_counter == 5:
        print("You can't save the money.")
        print(days_Counter)
    if owned_money >= needen_money:
        print(F"You saved the money for {days_Counter} days.")