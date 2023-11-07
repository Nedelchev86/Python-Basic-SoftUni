# всички карти е тестето

cards = "AKQJT98765432"
colors = "CSHD"

for i in range(len(colors)):
    for j in range(len(cards)):
        print(F"{cards[j]}  {colors[i]}")