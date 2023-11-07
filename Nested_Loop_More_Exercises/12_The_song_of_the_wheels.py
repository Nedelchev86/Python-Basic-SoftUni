control_sum = int(input())
count = 0
find = False

for a in range(1, 10):
  for b in range(1, 10):
    for c in range(1, 10):
      for d in range(1, 10):
        if a < b and c > d and (a * b) +  (c * d) == control_sum:
          count +=1
          print(F"{a}{b}{c}{d}", end=" ")
          if count == 4:
            password = (F"{a}{b}{c}{d}")
            find = True
print()
if find:

  print(F"Password: {password}")
else:
  print("No!")