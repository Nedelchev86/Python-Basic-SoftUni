
groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups):
    group = int(input())
    if group < 6:
        musala += group
    elif group < 13:
        monblan += group
    elif group < 26:
        kilimanjaro += group
    elif group < 41:
        k2 += group
    else:
        everest += group
total_people = musala + monblan + kilimanjaro + k2 + everest

print(F"{musala / total_people *100:.2F}%")
print(F"{monblan / total_people *100:.2F}%")
print(F"{kilimanjaro / total_people *100:.2F}%")
print(F"{k2 / total_people *100:.2F}%")
print(F"{everest / total_people *100:.2F}%")