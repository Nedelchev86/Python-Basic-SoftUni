fail = int(input())
bad_score = 0
name = input()
problems = 0
total_score = 0
last_name = ""

while name != "Enough":
    problems += 1
    score = int(input())
    total_score += score
    if score <= 4:
        bad_score +=1
    if bad_score >= fail:
        print(F"You need a break, {bad_score} poor grades.")
        break
    last_name = name
    name = input()
else:
    print(F"Average score: {total_score / problems:.2F}")
    print(F"Number of problems: {problems}")
    print(F"Last problem: {last_name}")


