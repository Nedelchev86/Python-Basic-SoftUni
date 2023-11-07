import  math
guests = int(input())
budget = int(input())

mufin_needed = math.ceil(guests /3)
eggs_needen = math.ceil(guests * 2)

money_needed =  (mufin_needed * 4) + ( eggs_needen * 0.45)
money_left = budget - money_needed
if money_left >=0:
    print(F"Lyubo bought {mufin_needed} Easter bread and {eggs_needen} eggs.")
    print(F"He has {money_left:.2F} lv. left.")
else:
    money_left = abs(money_left)
    print("Lyubo doesn't have enough money.")
    print(F"He needs {money_left:.2F} lv. more.")


