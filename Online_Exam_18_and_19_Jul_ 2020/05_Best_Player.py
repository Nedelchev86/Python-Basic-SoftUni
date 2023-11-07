name = input()
best_player = ""
hetrick = False
more_goals = 0

while name != "END":
    goals = int(input())
    if more_goals < goals:
        more_goals = goals
        best_player = name
    if goals >= 3:
        hetrick = True
    if goals >= 10:
        break

    name = input()

print(F"{best_player} is the best player!")
if hetrick:
    print(F"He has scored {more_goals} goals and made a hat-trick !!!")
else:
    print(F"He has scored {more_goals} goals.")
