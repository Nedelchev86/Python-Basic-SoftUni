# От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
#  На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
#  За всеки един посетител на отделен ред – дейността във фитнеса – текст ("Back", "Chest", "Legs", "Abs",
# "Protein shake" или "Protein bar")

visitors = int(input())
back = 0
chest = 0
legs = 0
abs_training  = 0
protein_shake = 0
protein_bar = 0

for i in range(visitors):
    training = input()
    if training == "Back":
        back +=1
    elif training == "Chest":
        chest += 1
    elif training == "Legs":
        legs += 1
    elif training == "Abs":
        abs_training += 1
    elif training == "Protein shake":
        protein_shake += 1
    elif training == "Protein bar":
        protein_bar += 1
training_peope = back + chest + legs + abs_training

print(F"{back} - back")
print(F"{chest} - chest")
print(F"{legs} - legs")
print(F"{abs_training} - abs")
print(F"{protein_shake} - protein shake")
print(F"{protein_bar} - protein bar")
print(F"{training_peope / visitors * 100:.2F}% - work out")
print(F"{100 - (training_peope / visitors * 100):.2F}% - protein")