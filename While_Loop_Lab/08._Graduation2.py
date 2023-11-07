name = input()
grade = 1
fail = 0
avarage = 0

while True:
    current_input = float(input())
    if current_input < 4:
        fail += 1
        if fail >= 2:
            break
        continue
    grade += 1
    avarage += current_input
    if grade > 12:
        break

if fail >= 2:
    print(F"{name} has been excluded at {grade} grade")
else:
    print(F"{name} graduated. Average grade: {avarage /12:.2F}")
