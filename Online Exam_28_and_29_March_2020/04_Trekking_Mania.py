groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0


for i in range(1, groups + 1):
  people = int(input())
  if people <= 5:
    musala +=  people
  elif people <= 12:
    monblan += people
  elif people <=25:
    kilimanjaro += people
  elif people <=40:
    k2 += people
  else:
    everest += people

all_people = musala + monblan + kilimanjaro + k2 + everest
print(F"{musala / all_people * 100:.2F}%")
print(F"{monblan / all_people * 100:.2F}%")
print(F"{kilimanjaro / all_people * 100:.2F}%")
print(F"{k2 / all_people * 100:.2F}%")
print(F"{everest / all_people * 100:.2F}%")