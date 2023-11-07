
win = 0
lost = 0
even = 0

for i in range (1, 4):
    mach = input()
    if mach[0] > mach[2]:
        win += 1
    elif mach[0] < mach[2]:
        lost += 1
    else:
        even +=1
print(F"Team won {win} games.")
print(F"Team lost {lost} games.")
print(F"Drawn games: {even}")
