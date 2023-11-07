floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    for room in range(0, rooms):
        if floor == floors:
            print(F"L{floor}{room} ", end='')
            continue
        if floor % 2 == 0:
            print(F"O{floor}{room} ", end='')
        else:
            print(F"A{floor}{room} ", end='')
    print("")