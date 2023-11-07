going = True
while going:
    destination = input()
    if destination == "End":
        going = False
        break
    budget = float(input())
    while budget > 0:
        money = float(input())
        budget -= money
    print(F"Going to {destination}!")