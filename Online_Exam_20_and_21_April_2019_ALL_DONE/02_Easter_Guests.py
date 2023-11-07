# Вход
# От конзолата се четат 2 реда:
#  На първия ред са броят на гостите – цяло число в интервала [0 ... 200000]
#  На втория ред е бюджетът с който разполага Любо – цяло число в интервала [0 ... 200000]
import math

guests = int(input())
budget = int(input())

number_cakes = math.ceil(guests / 3)
number_eggs = guests * 2

money_for_cakes =  number_cakes * 4
money_for_eggs = number_eggs * 0.45
total = money_for_eggs + money_for_cakes

if budget >= total:
    print(F"Lyubo bought {number_cakes} Easter bread and {number_eggs} eggs.")
    print(F"He has {budget - total:.2F} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(F"He needs {total - budget:.2F} lv. more.")
