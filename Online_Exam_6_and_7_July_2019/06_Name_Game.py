score = 0
max_score = 0
best_player = ""
max_score = 0

while True:
    name = input()
    if name == "Stop":
        break
    score = 0
    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            score += 10
        else:
            score +=2

    if score >= max_score:
        max_score = score
        best_player = name

print(F"The winner is {best_player} with {max_score} points!")

