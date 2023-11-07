
cake_number = int(input())
total_score = 0
best_score = 0
best_cooker = ""

for i in range(cake_number):
    name = input()
    command = input()
    while command != "Stop":
        score = int(command)
        total_score += score
        command = input()
    print(f"{name} has {total_score} points.")
    if total_score > best_score:
        best_score = total_score
        best_cooker = name
        print(F"{best_cooker} is the new number 1!")

    total_score = 0
print(F"{best_cooker} won competition with {best_score} points!")
