player_name = input()

points = 301
ok_throws = 0
nok_throw = 0

while True:
    tmp_points = 0
    sector = input()
    if sector == "Retire":
        print(F"{player_name} retired after {nok_throw} unsuccessful shots.")
    throw_points = int(input())
    if sector == "Single":
        tmp_points = throw_points
    elif sector == "Double":
        tmp_points = 2 * throw_points
    else:
        tmp_points = 3 * throw_points

    if tmp_points <= points:
        ok_throws += 1
        points -= tmp_points
    else:
        nok_throw += 1

    if points == 0:
        print(F"{player_name} won the leg with {ok_throws} shots.")
        break