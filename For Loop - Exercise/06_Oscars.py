
name = input()
score = float(input())
num_judge = int(input())
judge_total_score = 0
score_needed = (1250.5 - score)

for i in range(1, num_judge +1):
    judge_name = input()
    judge_score = float(input())
    judge_total_score += ((len(judge_name) * judge_score)/2)
    if judge_total_score >= score_needed:
        print(F"Congratulations, {name} got a nominee for leading role with {judge_total_score + score:.1F}!")
        break
if judge_total_score < score_needed:
    print(F"Sorry, {name} you need {score_needed - judge_total_score:.1F} more!")
