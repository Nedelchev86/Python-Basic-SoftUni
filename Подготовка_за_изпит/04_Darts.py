start_score = 301
bad_shoot = 0
player_name = input()
good_Shoot = 0

while start_score != 0:
    sector = input()
    if sector == "Retire":
        print(F"{player_name} retired after {bad_shoot} unsuccessful shots.")
        break
    score = int(input())
    if sector == "Single":
        score = score
    elif sector == "Double":
        score = 2 * score
    else:
        score = 3 * score
    start_score -= score
    if start_score < 0:
        bad_shoot += 1
        start_score += score
    else:
        good_Shoot += 1
else:
    print(F"{player_name} won the leg with {good_Shoot} shots.")