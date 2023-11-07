# 1. Брой екскурзии за море – цяло число в интервала [1… 500]
# 2. Брой екскурзии за планина – цяло число в интервала [1… 500

number_sea = int(input())
number_mountain = int(input())
profit = 0

while True:
    package = input()
    if package == "Stop":
        break
    if package == "sea" and number_sea > 0:
        number_sea -= 1
        profit += 680
    elif package == "mountain" and number_mountain > 0:
        number_mountain -= 1
        profit += 499
    if number_sea == 0 and number_mountain == 0:
        print("Good job! Everything is sold.")
        break
print(F"Profit: {profit} leva.")
