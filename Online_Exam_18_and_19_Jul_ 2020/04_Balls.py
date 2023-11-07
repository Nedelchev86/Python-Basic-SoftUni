import math
n = int(input())

result = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0


for i in range(0, n):
    ball = input()
    if ball == "red":
        red += 1
        result += 5
    elif ball == "orange":
        orange += 1
        result += 10
    elif ball == "yellow":
        yellow += 1
        result += 15
    elif ball == "white":
        white += 1
        result += 20
    elif ball == "black":
        black += 1
        result = math.floor(result / 2)
    else:
        other += 1

print(F"Total points: {result}")
print(F"Red balls: {red}")
print(F"Orange balls: {orange}")
print(F"Yellow balls: {yellow}")
print(F"White balls: {white}")
print(F"Other colors picked: {other}")
print(F"Divides from black balls: {black}")