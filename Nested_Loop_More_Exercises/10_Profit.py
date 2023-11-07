one = int(input())
two = int(input())
five = int(input())
sum = int(input())

for i in range(0, one + 1):
  for j in range(0, two + 1):
    for l in range(0, five + 1):
      if (i + (j * 2) + (l * 5)) == sum:
        print(F"{i} * 1 lv. + {j} * 2 lv. + {l} * 5 lv. = {sum} lv.")