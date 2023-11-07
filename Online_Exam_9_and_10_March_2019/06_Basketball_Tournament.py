win = 0
lost = 0
total_count = 0
while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break
    match = int(input())
    count = 0
    for i in range(match):
        team_a = int(input())
        team_b = int(input())
        count += 1
        if team_a > team_b:
            win += 1
            print(F"Game {count} of tournament {tournament_name}: win with {team_a - team_b} points.")
        else:
            lost += 1
            print(F"Game {count} of tournament {tournament_name}: lost with {team_b - team_a} points.")
    total_count += count
print(F"{win / total_count * 100:.2F}% matches win")
print(F"{lost / total_count * 100:.2F}% matches lost")
