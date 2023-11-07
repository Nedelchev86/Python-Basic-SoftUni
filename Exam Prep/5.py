max_goal = 0
best_player = ""

while True:
    name = input()
    if name == "END":
        break
    goal = int(input())
    if goal > max_goal:
        best_player = name
        max_goal = goal
    if max_goal >= 10:
        break
print(F"{best_player} is the best player!")
if max_goal >= 3:
    print(F"He has scored {max_goal} goals and made a hat-trick !!!")
else:
    print(F"He has scored {max_goal} goals.")