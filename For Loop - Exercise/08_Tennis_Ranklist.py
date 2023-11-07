from math import  floor

tournaments = int(input())
starting_points = int(input())

win_tournaments = 0
gained_points = 0

for _ in range(tournaments):
    tournament = input()

    if tournament == "W":
        win_tournaments  +=1
        gained_points +=2000
    elif tournament == "F":
        gained_points += 1200
    else:
        gained_points += 720
print(F"Final points: {starting_points + gained_points}")
print(F"Average points: {floor(gained_points / tournaments)}")
print(F"{win_tournaments / tournaments *100:.2F}%")