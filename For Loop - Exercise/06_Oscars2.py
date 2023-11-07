
actor = input()
points = float(input())
judges = int(input())
judge_total_score = 0

MAX_POINTS = 1250.5

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())
    points += len(judge_name) * judge_points /2
    if points > MAX_POINTS:
        print(F"Congratulations, {actor} got a nominee for leading role with {points:.1F}!")
        break
else:
    print(F"Sorry, {actor} you need {MAX_POINTS - points:.1F} more!")
