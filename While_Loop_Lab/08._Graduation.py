name = input()
bad_score = 0
grade = 1
total = 0

while grade <= 12:
    evaluation = float(input())
    grade += 1
    total += evaluation
    if evaluation < 4:
        bad_score += 1
        total -= evaluation
        grade -= 1
        if bad_score >= 2:
            print(F"{name} has been excluded at {grade} grade")
            break
if grade >= 12:
    print(F"{name} graduated. Average grade: {total / 12:.2F}")



