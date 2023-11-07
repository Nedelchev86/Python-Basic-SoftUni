first = int(input())
second = int(input())
magic = int(input())
count = 0

for i in range(first, second +1):
  for k in range(first, second +1):
    count += 1
    if i + k == magic:
      print(F"Combination N:{count} ({i} + {k} = {magic})")
      exit()

print(F"{count} combinations - neither equals {magic}")