
club = input()
num = int(input())
win = 0
draw = 0
lost = 0
points = 0

for i in range (0, num):
    result = input()
    if result == "W":
        win += 1
        points += 3
    elif result == "D":
        draw +=1
        points += 1
    else:
        lost += 1

if num > 0:
    print(f"{club} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {win}")
    print(f"## D: {draw}")
    print(f"## L: {lost}")
    print(f"Win rate: {win / num * 100:.2F}%")
else:
    print(f"{club} hasn't played any games during this season.")