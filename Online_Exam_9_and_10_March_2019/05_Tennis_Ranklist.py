# От конзолата първо се четат два реда:
#  Брой турнири, в които е участвал – цяло число в интервала [1…20]
#  Начален брой точки в ранглистата - цяло число в интервала [1...4000]
import math

number = int(input())
first_score = int(input())
score = 0
win = 0
for i in range (number):
    rank = input()
    if rank == "W":
        score += 2000
        win += 1
    elif rank == "F":
        score += 1200
    else:
        score += 720

print(F"Final points: {score + first_score}")
print(F"Average points: {math.floor(score / number)}")
print(F"{win / number * 100:.2F}%")