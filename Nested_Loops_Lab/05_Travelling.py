money = 0

while True:
    town = input()
    if town == "End":
        break
    trip_cost = float(input())
    while True:
        sum = float(input())
        money += sum
        if money >= trip_cost:
            print(F"Going to {town}!")
            money = 0
            break
