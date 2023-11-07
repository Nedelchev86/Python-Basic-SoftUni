money_for_vacantion = float(input())
money_have = float(input())
enought = True
days = 0
spending_money = 0

while enought:
    days += 1
    what_to_do = input()
    dayli_money = float(input())
    if what_to_do == "spend":
        money_have -= dayli_money
        spending_money += 1
        if money_have < 0:
            money_have = 0
    else:
        money_have += dayli_money
        spending_money = 0
    if money_have >= money_for_vacantion:
        print(F"You saved the money for {days} days.")
        break
    if spending_money == 5:
        print(F"You can't save the money.")
        print(F"{days}")
        break
