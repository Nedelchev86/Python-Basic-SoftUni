
number = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0
for i in range(0, number):
    game = input()
    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        fornite += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1

print(F"Hearthstone - {(hearthstone / number) * 100:.2F}%")
print(F"Fornite - {(fornite / number) * 100:.2F}%")
print(F"Overwatch - {(overwatch / number) * 100:.2F}%")
print(F"Others - {(others  / number) * 100:.2F}%")
